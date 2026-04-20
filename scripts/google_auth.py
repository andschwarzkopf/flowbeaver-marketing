#!/usr/bin/env python3
"""
OAuth2 Authentication für Google APIs (GA4 + Google Ads).
Einmal ausführen, dann den Refresh Token in .env speichern.

Usage: python3 scripts/google_auth.py
"""

import os
import json
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes für GA4 und Google Ads
SCOPES = [
    'https://www.googleapis.com/auth/analytics.readonly',
    'https://www.googleapis.com/auth/adwords',
]

def main():
    # .env lesen
    env_path = Path(__file__).parent.parent / '.env'
    env_vars = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                env_vars[key.strip()] = val.strip()

    client_id = env_vars.get('GOOGLE_CLIENT_ID')
    client_secret = env_vars.get('GOOGLE_CLIENT_SECRET')

    if not client_id or not client_secret:
        print("Fehler: GOOGLE_CLIENT_ID und GOOGLE_CLIENT_SECRET muessen in .env stehen.")
        return

    # OAuth2 Client Config
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }

    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    credentials = flow.run_local_server(port=8091, prompt='consent')

    refresh_token = credentials.refresh_token

    print("\n=== Authentifizierung erfolgreich! ===\n")
    print(f"Refresh Token: {refresh_token}\n")

    # Refresh Token in .env schreiben
    env_content = env_path.read_text()
    env_content = env_content.replace(
        'GOOGLE_REFRESH_TOKEN=',
        f'GOOGLE_REFRESH_TOKEN={refresh_token}'
    )
    env_path.write_text(env_content)
    print("Refresh Token wurde in .env gespeichert.")
    print("Du kannst dieses Skript jetzt schliessen.")


if __name__ == '__main__':
    main()
