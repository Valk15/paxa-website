"""
PAXA TikTok Marketing API — Ad Management
Usage:
  python ads.py list --adgroup ADGROUP_ID
  python ads.py create --adgroup ADGROUP_ID --name "img2" --image-id IMAGE_ID --title "Your dog licks. Anxiety drops." --text "The neuroscience of calm."
  python ads.py pause --id AD_ID
  python ads.py enable --id AD_ID
"""
import sys
import json
import argparse
import requests
from config import BASE_URL, HEADERS, TIKTOK_ADVERTISER_ID, CALM_MAT, check_credentials


def list_ads(adgroup_id):
    url = f'{BASE_URL}/ad/get/'
    params = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'adgroup_ids': json.dumps([adgroup_id]),
        'fields': json.dumps(['ad_id', 'ad_name', 'status', 'ad_format'])
    }
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return
    ads = data['data']['list']
    if not ads:
        print("No ads found.")
        return
    print(f"\n{'ID':<25} {'Name':<35} {'Status':<12} {'Format'}")
    print('-' * 85)
    for a in ads:
        print(f"{a['ad_id']:<25} {a['ad_name']:<35} {a['status']:<12} {a.get('ad_format', 'N/A')}")


def get_image_ids():
    """List all uploaded image assets in the ad account."""
    url = f'{BASE_URL}/file/image/ad/get/'
    params = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'image_type': 'CREATIVE_MATERIAL'
    }
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return
    images = data['data']['list']
    if not images:
        print("No images found. Upload creatives in TikTok Ads Manager → Assets → Creative Library first.")
        return
    print(f"\n{'Image ID':<30} {'Name':<40} {'Size'}")
    print('-' * 85)
    for img in images:
        print(f"{img['image_id']:<30} {img.get('file_name', 'N/A'):<40} {img.get('size', 'N/A')}")


def create_image_ad(adgroup_id, ad_name, image_id, title, ad_text):
    url = f'{BASE_URL}/ad/create/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'adgroup_id': adgroup_id,
        'ad_name': ad_name,
        'ad_format': 'SINGLE_IMAGE',
        'image_ids': [image_id],
        'ad_text': ad_text,
        'call_to_action': 'SHOP_NOW',
        'landing_page_url': CALM_MAT['url'],
        'display_name': 'PAXA',
        'operation_status': 'ENABLE'
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return None
    ad_id = data['data']['ad_id']
    print(f"[OK] Ad created: {ad_id}")
    print(f"     Name: {ad_name} | Text: {ad_text}")
    return ad_id


def set_ad_status(ad_id, status):
    url = f'{BASE_URL}/ad/status/update/'
    payload = {
        'advertiser_id': TIKTOK_ADVERTISER_ID,
        'ad_ids': [ad_id],
        'operation_status': status
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    data = r.json()
    if data.get('code') != 0:
        print(f"[ERROR] {data.get('message')}")
        return False
    print(f"[OK] Ad {ad_id} → {status}")
    return True


if __name__ == '__main__':
    if not check_credentials():
        sys.exit(1)

    parser = argparse.ArgumentParser(description='PAXA TikTok Ad Manager')
    subparsers = parser.add_subparsers(dest='command')

    p_list = subparsers.add_parser('list')
    p_list.add_argument('--adgroup', required=True)

    subparsers.add_parser('images')

    p_create = subparsers.add_parser('create')
    p_create.add_argument('--adgroup', required=True)
    p_create.add_argument('--name', required=True)
    p_create.add_argument('--image-id', required=True)
    p_create.add_argument('--text', required=True)

    p_pause = subparsers.add_parser('pause')
    p_pause.add_argument('--id', required=True)

    p_enable = subparsers.add_parser('enable')
    p_enable.add_argument('--id', required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_ads(args.adgroup)
    elif args.command == 'images':
        get_image_ids()
    elif args.command == 'create':
        create_image_ad(args.adgroup, args.name, args.image_id, '', args.text)
    elif args.command == 'pause':
        set_ad_status(args.id, 'DISABLE')
    elif args.command == 'enable':
        set_ad_status(args.id, 'ENABLE')
    else:
        parser.print_help()
