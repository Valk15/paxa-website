"""
PAXA — Launch Calm Mat Purchase Campaign
One-command campaign setup. Run once to create the full campaign structure.

Usage:
  python launch_calm_mat.py --budget 20 --adgroup-name "UK Broad 25-54"

What it creates:
  1. Campaign:  PAXA Calm Mat — Purchase (£BUDGET/day)
  2. Ad Group:  UK Broad 25-54 (Purchase optimisation, TikTok feed, UK)
  3. Saves IDs to campaign_ids.json for future reference
"""
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
import campaigns as c
import adgroups as ag
from config import check_credentials


def launch(daily_budget, adgroup_name):
    if not check_credentials():
        sys.exit(1)

    print('\n══ PAXA CALM MAT — CAMPAIGN LAUNCH ══════════════════')
    print(f'Budget: £{daily_budget}/day | Target: UK 25-54 Broad')
    print(f'Objective: Purchase | Destination: calm-mat-landing')
    print('─────────────────────────────────────────────────────\n')

    # Step 1: Create campaign
    campaign_name = f'PAXA Calm Mat — Purchase [{datetime.today().strftime("%d %b %Y")}]'
    campaign_id = c.create_campaign(campaign_name, daily_budget)
    if not campaign_id:
        print('[FAILED] Could not create campaign.')
        sys.exit(1)

    # Step 2: Create ad group
    adgroup_id = ag.create_adgroup(campaign_id, adgroup_name, daily_budget)
    if not adgroup_id:
        print('[FAILED] Could not create ad group.')
        sys.exit(1)

    # Step 3: Save IDs
    ids = {
        'campaign_id': campaign_id,
        'campaign_name': campaign_name,
        'adgroup_id': adgroup_id,
        'adgroup_name': adgroup_name,
        'daily_budget': daily_budget,
        'created_at': datetime.today().isoformat()
    }
    output_path = Path(__file__).parent / 'campaign_ids.json'
    with open(output_path, 'w') as f:
        json.dump(ids, f, indent=2)

    print('\n══ DONE ══════════════════════════════════════════════')
    print(f'Campaign ID : {campaign_id}')
    print(f'Ad Group ID : {adgroup_id}')
    print(f'\nNext step — add your creatives:')
    print(f'  1. python ads.py images              ← get your image IDs from Creative Library')
    print(f'  2. python ads.py create --adgroup {adgroup_id} --name "img2" --image-id IMAGE_ID --text "Your ad text"')
    print(f'  3. Repeat for each creative (add 2-3 max)')
    print(f'\nMonitor performance:')
    print(f'  python reports.py daily')
    print(f'  python reports.py rules    ← runs kill/scale rules automatically')
    print('═══════════════════════════════════════════════════════\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Launch PAXA Calm Mat Purchase Campaign')
    parser.add_argument('--budget', type=float, default=20.0, help='Daily budget in GBP')
    parser.add_argument('--adgroup-name', default='UK Broad 25-54')
    args = parser.parse_args()
    launch(args.budget, args.adgroup_name)
