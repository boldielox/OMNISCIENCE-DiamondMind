# config/constants.py
API_BASE_URL = "https://v1.baseball.api-sports.io"
MLB_LEAGUE_ID = 12

HEADERS = {
    "x-apisports-key": os.getenv("API_SPORTS_KEY")
}
