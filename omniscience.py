# omniscience.py
import typer
from app.dashboard import launch_dashboard
from model.train_model import train
from data.ingest.odds_fetcher import fetch_odds

app = typer.Typer()

@app.command()
def dashboard():
    """Launch Omniscience Streamlit UI"""
    launch_dashboard()

@app.command()
def train_model():
    """Train Omniscience Betting Model"""
    train()

@app.command()
def fetch():
    """Manually Fetch Odds Data"""
    fetch_odds()

if __name__ == "__main__":
    app()
