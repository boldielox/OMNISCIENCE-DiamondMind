# features/signal_rules.py
from features.indicators import calculate_rsi, bollinger_bands
from features.fibonacci import get_fibonacci_levels
import pandas as pd

def generate_signals(df, price_col="implied_prob_home", rsi_col="RSI", volume_col="volume"):
    """
    Detects bet signals using fib levels, RSI, volume anomalies.
    Returns a DataFrame with 'signal' and 'reason' columns.
    """

    signals = []

    high = df[price_col].max()
    low = df[price_col].min()
    fib_levels = get_fibonacci_levels(high, low)

    # Precompute RSI if not already
    if rsi_col not in df.columns:
        df[rsi_col] = calculate_rsi(df[price_col])

    for i, row in df.iterrows():
        price = row[price_col]
        rsi = row[rsi_col]
        volume = row.get(volume_col, None)

        signal = None
        reason = []

        # --- Fibonacci Reversal Zone ---
        for level, target in fib_levels.items():
            tolerance = 0.003  # ~0.3% wiggle
            if abs(price - target) / target < tolerance:
                reason.append(f"Price near Fib level {level}")
                break

        # --- RSI Extremes ---
        if rsi is not None:
            if rsi > 70:
                reason.append("RSI overbought (>70)")
            elif rsi < 30:
                reason.append("RSI oversold (<30)")

        # --- Volume Spike (optional) ---
        if volume_col in df.columns:
            rolling_avg = df[volume_col].rolling(10).mean().iloc[i]
            if rolling_avg > 0 and volume > 1.5 * rolling_avg:
                reason.append("Volume spike detected")

        # --- Signal Assignment ---
        if len(reason) >= 2:
            signal = "ENTRY"
        elif len(reason) == 1:
            signal = "WATCH"

        signals.append({
            "date": row.get("date", i),
            "price": price,
            "signal": signal,
            "reason": "; ".join(reason)
        })

    return pd.DataFrame(signals)
