# app/explain_engine.py

def explain_decision(game_id, team_home, team_away, decision):
    """
    Generates human-readable explanation for a betting decision.
    """
    if not decision:
        return f"No betting signal was triggered for game ID {game_id}."

    bet = decision['bet_type']
    side = decision['side']
    confidence = decision['confidence']
    stake = decision['stake_pct']
    rationale = decision['rationale']

    team_selected = team_home if side == "Home" else team_away
    direction = "to win" if bet == "Moneyline" else ("to cover the spread" if bet == "Run Line" else f"on the {side.lower()} total")

    intro = f"🔍 **Bet Recommendation**: {team_selected} {direction} via {bet}\n\n"
    meta = f"🧠 **Confidence**: {int(confidence * 100)}%\n💸 **Stake**: {int(stake * 100)}% of bankroll\n\n"

    reasons = "\n".join([f"• {r}" for r in rationale])
    reason_section = f"📈 **Reasoning**:\n{reasons}"

    return intro + meta + reason_section
