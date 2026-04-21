"""
PAXA TikTok Marketing API — Config
Reads credentials from environment variables or .env file.
"""
import os
from pathlib import Path

# Load .env file if present
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

TIKTOK_ACCESS_TOKEN = os.environ.get('TIKTOK_ACCESS_TOKEN', '')
TIKTOK_ADVERTISER_ID = os.environ.get('TIKTOK_ADVERTISER_ID', '')
TIKTOK_APP_ID = os.environ.get('TIKTOK_APP_ID', '')

BASE_URL = 'https://business-api.tiktok.com/open_api/v1.3'

HEADERS = {
    'Access-Token': TIKTOK_ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# PAXA Calm Mat product details
CALM_MAT = {
    'name': 'PAXA Calm Mat Bundle of 2',
    'price': 34,
    'currency': 'GBP',
    'url': 'https://paxapet.co.uk/calm-mat-landing',
    'pixel_id': 'D7J2053C77U8847ELUI0',
    'shopify_url': 'https://paxa-7714.myshopify.com/cart/53536507068753:1'
}

def check_credentials():
    missing = []
    if not TIKTOK_ACCESS_TOKEN:
        missing.append('TIKTOK_ACCESS_TOKEN')
    if not TIKTOK_ADVERTISER_ID:
        missing.append('TIKTOK_ADVERTISER_ID')
    if missing:
        print(f"[ERROR] Missing credentials: {', '.join(missing)}")
        print("Add them to your .env file. See .env.example for format.")
        return False
    return True
