"""
PAXA TikTok Marketing API — Ad Group Management
Usage:
  python adgroups.py list --campaign CAMPAIGN_ID
  python adgroups.py create --campaign CAMPAIGN_ID --name "UK Broad 25-55" --budget 20
  python adgroups.py pause --id ADGROUP_ID
  python adgroups.py enable --id ADGROUP_ID
"""
import sys
import json
import argparse
import requests
from config import BASE_URL, HEADERS, TIKTOK_ADVERTISER_ID, CALM_MAT, check_credentials


def list_adgroups(campaign_id):
    url = f'{BASE_URL}/adgroup/get/'
    params = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'campaign_ids': json.dumps([campaign_id]),
        'fields': json.dumps(['adgroup_id', 'adgroup_name', 'status', 'budget'])
    }
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return
    groups = data['data']['list']
    if not groups:
        print("No ad groups found.")
        return
    print(f"\n{'ID':<25} {'Name':<35} {'Status':<12} {'Budget/day'}")
    print('-' * 80)
    for g in groups:
        print(f"{g['adgroup_id']:<25} {g['adgroup_name']:<35} {g['status']:<12} £{g.get('budget', 'N/A')}")


def create_adgroup(campaign_id, name, daily_budget):
    url = f'{BASE_URL}/adgroup/create/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'campaign_id': campaign_id,
        'adgroup_name': name,
        'promotion_type': 'WEBSITE',
        'placement_type': 'PLACEMENT_TYPE_AUTOMATIC',
        'placements': ['PLACEMENT_TIKTOK'],
        'location_ids': ['GB'],                      # UK only
        'age_groups': ['AGE_25_34', 'AGE_35_44', 'AGE_45_54'],
        'gender': 'GENDER_UNLIMITED',
        'optimization_goal': 'CONVERT',
        'pixel_id': CALM_MAT['pixel_id'],
        'external_action': 'COMPLETE_PAYMENT',       # Purchase event
        'landing_page_url': CALM_MAT['url'],
        'budget_mode': 'BUDGET_MODE_DAY',
        'budget': float(daily_budget),
        'schedule_type': 'SCHEDULE_START_END',
        'schedule_start_time': '2026-04-21 00:00:00',
        'schedule_end_time': '2026-12-31 23:59:59',
        'billing_event': 'OCPM',
        'bid_type': 'BID_TYPE_NO_BID',
        'operation_status': 'ENABLE'
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return None
    adgroup_id = data['data']['adgroup_id']
    print(f"[OK] Ad group created: {adgroup_id}")
    print(f"     Name: {name} | Budget: £{daily_budget}/day | Target: UK 25-54 Broad")
    return adgroup_id


def set_adgroup_status(adgroup_id, status):
    url = f'{BASE_URL}/adgroup/status/update/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'adgroup_ids': [adgroup_id],
        'operation_status': status
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return False
    print(f"[OK] Ad group {adgroup_id} → {status}")
    return True


if __name__ == '__main__':
    if not check_credentials():
        sys.exit(1)

    parser = argparse.ArgumentParser(description='PAXA TikTok Ad Group Manager')
    subparsers = parser.add_subparsers(dest='command')

    p_list = subparsers.add_parser('list')
    p_list.add_argument('--campaign', required=True)

    p_create = subparsers.add_parser('create')
    p_create.add_argument('--campaign', required=True)
    p_create.add_argument('--name', default='UK Broad 25-54')
    p_create.add_argument('--budget', required=True, type=float)

    p_pause = subparsers.add_parser('pause')
    p_pause.add_argument('--id', required=True)

    p_enable = subparsers.add_parser('enable')
    p_enable.add_argument('--id', required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_adgroups(args.campaign)
    elif args.command == 'create':
        create_adgroup(args.campaign, args.name, args.budget)
    elif args.command == 'pause':
        set_adgroup_status(args.id, 'DISABLE')
    elif args.command == 'enable':
        set_adgroup_status(args.id, 'ENABLE')
    else:
        parser.print_help()
