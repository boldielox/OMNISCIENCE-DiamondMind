# model/feedback_loop.py
import json
import os

HISTORY_PATH = "data/raw_data/bet_history.json"

def log_bet_result(game_id, result, actual_outcome):
    """
    Store result for future model feedback
    """
    if not os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "w") as f:
            json.dump({}, f)

    with open(HISTORY_PATH, "r+") as f:
        history = json.load(f)
        history[game_id] = {
            "result": result,
            "outcome": actual_outcome,
            "timestamp": str(datetime.now())
        }
        f.seek(0)
        json.dump(history, f, indent=2)
        f.truncate()
