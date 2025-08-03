# data/ingest/odds_fetcher.py
import requests
import os
from datetime import datetime
from config.constants import API_BASE_URL, MLB_LEAGUE_ID, HEADERS

def fetch_odds(date=None, season="2024"):
    date = date or datetime.today().strftime("%Y-%m-%d")
    params = {
        "league": MLB_LEAGUE_ID,
        "season": season,
        "date": date,
        "bookmaker": 6,  # Pinnacle
        "bet": 1,        # Match Winner
    }

    print(f"📡 Fetching odds for {date}...")
    response = requests.get(f"{API_BASE_URL}/odds", headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json().get("response", [])
    print(f"✅ Retrieved {len(data)} entries.")
    return data
