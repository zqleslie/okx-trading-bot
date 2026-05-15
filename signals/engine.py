"""Signal generation engine."""
from signals.indicator import calculate_rsi, calculate_j


def generate_signal(prices: list[float], k_values: list[float], d_values: list[float]) -> dict:
    """Generate trading signal based on indicators."""
    rsi = calculate_rsi(prices)
    j = calculate_j(k_values, d_values)[-1]

    if j > 50:
        return {"signal": "HOLD", "reason": "J-value too high (overbought)"}
    if rsi > 70:
        return {"signal": "HOLD", "reason": "RSI overbought"}
    if rsi < 30:
        return {"signal": "BUY", "reason": "RSI oversold"}
    return {"signal": "NEUTRAL", "reason": "No clear signal"}
