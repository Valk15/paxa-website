"""
PAXA TikTok Marketing API — Campaign Management
Usage:
  python campaigns.py list
  python campaigns.py create --name "PAXA Calm Mat — Purchase" --budget 20
  python campaigns.py status --id CAMPAIGN_ID
"""
import sys
import json
import argparse
import requests
from config import BASE_URL, HEADERS, TIKTOK_ADVERTISER_ID, check_credentials


def list_campaigns():
    url = f'{BASE_URL}/campaign/get/'
    params = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'fields': json.dumps(['campaign_id', 'campaign_name', 'status', 'budget', 'objective_type'])
    }
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return
    campaigns = data['data']['list']
    if not campaigns:
        print("No campaigns found.")
        return
    print(f"\n{'ID':<25} {'Name':<40} {'Status':<12} {'Budget/day'}")
    print('-' * 90)
    for c in campaigns:
        print(f"{c['campaign_id']:<25} {c['campaign_name']:<40} {c['status']:<12} £{c.get('budget', 'N/A')}")


def create_campaign(name, daily_budget):
    url = f'{BASE_URL}/campaign/create/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'campaign_name': name,
        'objective_type': 'CONVERSIONS',
        'budget_mode': 'BUDGET_MODE_DAY',
        'budget': float(daily_budget),
        'operation_status': 'ENABLE'
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return None
    campaign_id = data['data']['campaign_id']
    print(f"[OK] Campaign created: {campaign_id}")
    print(f"     Name: {name} | Budget: £{daily_budget}/day")
    return campaign_id


def set_campaign_status(campaign_id, status):
    """status: ENABLE or DISABLE"""
    url = f'{BASE_URL}/campaign/status/update/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'campaign_ids': [campaign_id],
        'operation_status': status
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return False
    print(f"[OK] Campaign {campaign_id} → {status}")
    return True


if __name__ == '__main__':
    if not check_credentials():
        sys.exit(1)

    parser = argparse.ArgumentParser(description='PAXA TikTok Campaign Manager')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list')

    p_create = subparsers.add_parser('create')
    p_create.add_argument('--name', required=True)
    p_create.add_argument('--budget', required=True, type=float)

    p_status = subparsers.add_parser('status')
    p_status.add_argument('--id', required=True)
    p_status.add_argument('--set', choices=['ENABLE', 'DISABLE'])

    args = parser.parse_args()

    if args.command == 'list':
        list_campaigns()
    elif args.command == 'create':
        create_campaign(args.name, args.budget)
    elif args.command == 'status':
        if args.set:
            set_campaign_status(args.id, args.set)
        else:
            print("Use --set ENABLE or --set DISABLE")
    else:
        parser.print_help()
