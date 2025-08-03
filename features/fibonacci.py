# features/fibonacci.py
def get_fibonacci_levels(high, low):
    diff = high - low
    levels = {
        "0.0%": high,
        "23.6%": high - 0.236 * diff,
        "38.2%": high - 0.382 * diff,
        "50.0%": high - 0.5 * diff,
        "61.8%": high - 0.618 * diff,
        "78.6%": high - 0.786 * diff,
        "100.0%": low,
        "161.8%": low - 0.618 * diff,
        "261.8%": low - 1.618 * diff,
    }
    return levels
