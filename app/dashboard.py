# app/dashboard.py
import streamlit as st
from data.ingest.odds_fetcher import fetch_odds
from features.signal_rules import generate_signals
from features.bet_selector import decide_bet
from app.explain_engine import explain_decision
import pandas as pd

def launch_dashboard():
    st.set_page_config(page_title="Omniscience AI Betting Terminal", layout="wide")
    st.title("🎯 Omniscience AI Control Center")

    # --- Controls ---
    season = st.sidebar.selectbox("Season", ["2022", "2023", "2024", "2025"], index=2)
    date = st.sidebar.date_input("Select Date")
    market = st.sidebar.selectbox("Market", ["Moneyline", "Run Line", "Total"])
    fetch_now = st.sidebar.button("🔁 Run Analysis")

    if fetch_now:
        with st.spinner("Fetching and analyzing market..."):
            raw_odds = fetch_odds(date=date, season=season)
            games = []

            for match in raw_odds:
                try:
                    home = match['teams']['home']['name']
                    away = match['teams']['away']['name']
                    game_id = match['fixture']['id']

                    # Build fake implied prob series for demo (extend later)
                    df = pd.DataFrame({
                        "implied_prob_home": [1 / match['bookmakers'][0]['bets'][0]['values'][0]['odd']],
                        "volume": [match.get('statistics', {}).get('volume', 1.0)]
                    })

                    signals = generate_signals(df)
                    if not signals.empty and signals.iloc[0]["signal"] == "ENTRY":
                        decision = decide_bet(signals.iloc[0])
                        explanation = explain_decision(game_id, home, away, decision)

                        st.subheader(f"🧠 {away} @ {home}")
                        st.markdown(explanation)
                        st.markdown("---")

                        games.append({
                            "Game": f"{away} @ {home}",
                            "Side": decision["side"],
                            "Bet Type": decision["bet_type"],
                            "Confidence": decision["confidence"],
                            "Stake %": decision["stake_pct"]
                        })

                except Exception as e:
                    st.error(f"Failed to process one game: {e}")

            if games:
                st.dataframe(pd.DataFrame(games))
            else:
                st.warning("No strong signals found today.")
