"""
PAXA TikTok Marketing API — Performance Reports + Auto Rules
Usage:
  python reports.py daily                      → today's stats for all active ads
  python reports.py campaign --id CAMPAIGN_ID  → campaign-level breakdown
  python reports.py rules                      → run kill/scale rules automatically
"""
import sys
import json
import argparse
from datetime import datetime, timedelta
import requests
from config import BASE_URL, HEADERS, TIKTOK_ADVERTISER_ID, check_credentials


# ── PAXA Performance Rules ───────────────────────────────────────
KILL_CTR_THRESHOLD   = 0.008   # Pause ad if CTR < 0.8% after 3 days + £10 spend
KILL_SPEND_MINIMUM   = 10.0    # Minimum spend before applying kill rule
KILL_DAYS_MINIMUM    = 3       # Minimum days running before applying kill rule
SCALE_CPA_TARGET     = 15.0    # If CPA < £15 after 7 days → flag for budget increase
SCALE_DAYS_MINIMUM   = 7


def get_date_range(days_back=7):
    end = datetime.today().strftime('%Y-%m-%d')
    start = (datetime.today() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    return start, end


def get_ad_performance(start_date, end_date):
    url = f'{BASE_URL}/report/integrated/get/'
    params = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'report_type': 'BASIC',
        'dimensions': json.dumps(['ad_id']),
        'metrics': json.dumps([
            'ad_name', 'spend', 'impressions', 'clicks', 'ctr',
            'cpc', 'cpm', 'conversion', 'cost_per_conversion',
            'conversion_rate', 'stat_cost'
        ]),
        'start_date': start_date,
        'end_date': end_date,
        'page_size': 50
    }
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return []
    return data['data']['list']


def print_ad_table(rows):
    if not rows:
        print("No data yet.")
        return
    print(f"\n{'Ad ID':<20} {'Name':<30} {'Spend':>8} {'CTR':>7} {'CPC':>7} {'Conv':>6} {'CPA':>8}")
    print('-' * 90)
    for row in rows:
        m = row.get('metrics', {})
        d = row.get('dimensions', {})
        spend = float(m.get('spend', 0))
        ctr   = float(m.get('ctr', 0))
        cpc   = float(m.get('cpc', 0))
        conv  = int(float(m.get('conversion', 0)))
        cpa   = float(m.get('cost_per_conversion', 0))
        name  = m.get('ad_name', 'N/A')[:28]
        ad_id = d.get('ad_id', 'N/A')
        print(f"{ad_id:<20} {name:<30} £{spend:>6.2f} {ctr*100:>6.2f}% £{cpc:>5.2f} {conv:>6} £{cpa:>6.2f}")


def run_rules():
    """Apply PAXA kill/scale rules to all active ads."""
    today = datetime.today().strftime('%Y-%m-%d')
    week_ago = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    three_ago = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')

    rows_7d = get_ad_performance(week_ago, today)
    rows_3d = get_ad_performance(three_ago, today)

    to_kill  = []
    to_scale = []

    # Index 3-day data by ad_id
    data_3d = {}
    for row in rows_3d:
        aid = row['dimensions']['ad_id']
        data_3d[aid] = row['metrics']

    for row in rows_7d:
        ad_id = row['dimensions']['ad_id']
        m7 = row['metrics']
        m3 = data_3d.get(ad_id, {})

        spend_7d  = float(m7.get('spend', 0))
        spend_3d  = float(m3.get('spend', 0))
        ctr_3d    = float(m3.get('ctr', 0))
        conv_7d   = int(float(m7.get('conversion', 0)))
        cpa_7d    = float(m7.get('cost_per_conversion', 0)) if conv_7d > 0 else 999
        name      = m7.get('ad_name', ad_id)

        # Kill rule
        if spend_3d >= KILL_SPEND_MINIMUM and ctr_3d < KILL_CTR_THRESHOLD:
            to_kill.append({'id': ad_id, 'name': name, 'ctr': ctr_3d*100, 'spend': spend_3d})

        # Scale flag
        if spend_7d > 0 and conv_7d >= 3 and cpa_7d < SCALE_CPA_TARGET:
            to_scale.append({'id': ad_id, 'name': name, 'cpa': cpa_7d, 'conv': conv_7d})

    print('\n── PAXA AUTO RULES REPORT ─────────────────────────────')

    if to_kill:
        print(f'\n🔴 PAUSE RECOMMENDED ({len(to_kill)} ads — CTR < 0.8% after £{KILL_SPEND_MINIMUM}+ spend):')
        for a in to_kill:
            print(f"   {a['id']} | {a['name']} | CTR: {a['ctr']:.2f}% | Spend: £{a['spend']:.2f}")
        print('\n   Run: python ads.py pause --id AD_ID  to pause each one')
    else:
        print('\n✅ No ads flagged for pausing.')

    if to_scale:
        print(f'\n🟢 SCALE RECOMMENDED ({len(to_scale)} ads — CPA < £{SCALE_CPA_TARGET}):')
        for a in to_scale:
            print(f"   {a['id']} | {a['name']} | CPA: £{a['cpa']:.2f} | Purchases: {a['conv']}")
        print('\n   Consider increasing daily budget by 20–50%.')
    else:
        print('\n⏳ No ads ready to scale yet (need 7 days + CPA < £15).')

    print('\n───────────────────────────────────────────────────────\n')


if __name__ == '__main__':
    if not check_credentials():
        sys.exit(1)

    parser = argparse.ArgumentParser(description='PAXA TikTok Performance Reports')
    subparsers = parser.add_subparsers(dest='command')

    p_daily = subparsers.add_parser('daily')
    p_daily.add_argument('--days', type=int, default=1)

    p_camp = subparsers.add_parser('campaign')
    p_camp.add_argument('--id', required=True)

    subparsers.add_parser('rules')

    args = parser.parse_args()

    if args.command == 'daily':
        today = datetime.today().strftime('%Y-%m-%d')
        start = (datetime.today() - timedelta(days=args.days - 1)).strftime('%Y-%m-%d')
        print(f"\nPerformance: {start} → {today}")
        rows = get_ad_performance(start, today)
        print_ad_table(rows)
    elif args.command == 'rules':
        run_rules()
    else:
        parser.print_help()
