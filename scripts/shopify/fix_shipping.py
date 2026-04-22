"""
PAXA — Fix Shopify Shipping Zones
Adds United Kingdom with free shipping. Removes France if present.

Usage:
  python fix_shipping.py --check        ← see current zones
  python fix_shipping.py --fix          ← add UK free shipping
  python fix_shipping.py --fix --remove-france  ← add UK + remove France

Requires in .env:
  SHOPIFY_ACCESS_TOKEN=your_admin_api_token
  SHOPIFY_SHOP_DOMAIN=ph6pk1-fq.myshopify.com
"""
import sys
import json
import argparse
import requests
from pathlib import Path

# ── Load .env ─────────────────────────────────────────────────────
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                import os; os.environ.setdefault(k.strip(), v.strip())

import os
SHOP    = os.environ.get('SHOPIFY_SHOP_DOMAIN', 'ph6pk1-fq.myshopify.com')
TOKEN   = os.environ.get('SHOPIFY_ACCESS_TOKEN', '')
API_VER = '2024-01'
BASE    = f'https://{SHOP}/admin/api/{API_VER}'
HEADERS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}


def check_token():
    if not TOKEN:
        print('[ERROR] SHOPIFY_ACCESS_TOKEN missing from .env')
        print('Get it from: Shopify Admin → Settings → Apps and sales channels → Develop apps → Create app → Admin API access token')
        sys.exit(1)


def get_zones():
    r = requests.get(f'{BASE}/shipping_zones.json', headers=HEADERS)
    if r.status_code != 200:
        print(f'[ERROR] {r.status_code}: {r.text}')
        return []
    return r.json().get('shipping_zones', [])


def print_zones(zones):
    if not zones:
        print('No shipping zones found.')
        return
    print(f'\n{"Zone":<25} {"Countries":<30} {"Rates"}')
    print('-' * 70)
    for z in zones:
        countries = ', '.join(c['code'] for c in z.get('countries', []))
        rates = len(z.get('price_based_shipping_rates', []))
        print(f"{z['name']:<25} {countries:<30} {rates} price rate(s)")
        for rate in z.get('price_based_shipping_rates', []):
            print(f"  └─ {rate['name']}: £{rate['price']}")


def add_uk_free_shipping():
    """Create UK shipping zone with free shipping rate."""
    # Step 1: Create the zone
    payload = {
        'shipping_zone': {
            'name': 'United Kingdom',
            'countries': [{'code': 'GB'}]
        }
    }
    r = requests.post(f'{BASE}/shipping_zones.json', headers=HEADERS, json=payload)

    if r.status_code == 201:
        zone = r.json()['shipping_zone']
        zone_id = zone['id']
        print(f'[OK] Shipping zone created: United Kingdom (ID: {zone_id})')
    elif r.status_code == 422:
        # Zone might already exist
        err = r.json()
        if 'already' in str(err).lower() or 'taken' in str(err).lower():
            print('[INFO] UK zone already exists — adding free rate to existing zone')
            zones = get_zones()
            zone = next((z for z in zones if 'GB' in [c['code'] for c in z.get('countries', [])]), None)
            if not zone:
                print('[ERROR] Could not find existing UK zone')
                return
            zone_id = zone['id']
        else:
            print(f'[ERROR] {r.status_code}: {r.text}')
            return
    else:
        print(f'[ERROR] {r.status_code}: {r.text}')
        return

    # Step 2: Add free shipping rate to the zone
    rate_payload = {
        'price_based_shipping_rate': {
            'name': 'Free UK Delivery',
            'price': '0.00',
            'min_order_subtotal': None,
            'max_order_subtotal': None
        }
    }
    r2 = requests.post(
        f'{BASE}/shipping_zones/{zone_id}/price_based_shipping_rates.json',
        headers=HEADERS,
        json=rate_payload
    )
    if r2.status_code == 201:
        print('[OK] Free UK Delivery rate added (£0.00, no minimum order)')
    else:
        print(f'[ERROR] Could not add rate: {r2.status_code}: {r2.text}')
        return

    print('\n✅ UK free shipping is live. Test it at:')
    print('   https://paxapet.com/products/paxa-calm-mat-bundle-of-2')
    print('   Add to cart → checkout → enter UK address → confirm £0 shipping\n')


def remove_france():
    """Remove France shipping zone."""
    zones = get_zones()
    france = next((z for z in zones if 'FR' in [c['code'] for c in z.get('countries', [])]), None)
    if not france:
        print('[INFO] No France zone found — nothing to remove')
        return
    r = requests.delete(f'{BASE}/shipping_zones/{france["id"]}.json', headers=HEADERS)
    if r.status_code == 200:
        print(f'[OK] France shipping zone removed')
    else:
        print(f'[ERROR] {r.status_code}: {r.text}')


if __name__ == '__main__':
    check_token()

    parser = argparse.ArgumentParser(description='PAXA Shopify Shipping Fix')
    parser.add_argument('--check', action='store_true', help='Show current shipping zones')
    parser.add_argument('--fix', action='store_true', help='Add UK free shipping zone')
    parser.add_argument('--remove-france', action='store_true', help='Remove France shipping zone')
    args = parser.parse_args()

    if args.check:
        zones = get_zones()
        print_zones(zones)
    elif args.fix:
        add_uk_free_shipping()
        if args.remove_france:
            remove_france()
        print('\nCurrent zones after fix:')
        print_zones(get_zones())
    else:
        parser.print_help()
