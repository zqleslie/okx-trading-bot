"""Technical indicators module."""


def calculate_rsi(prices: list[float], period: int = 14) -> float:
    """Calculate Relative Strength Index."""
    deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def calculate_j(k_values: list[float], d_values: list[float]) -> list[float]:
    """Calculate J value from K and D."""
    return [3 * k - 2 * d for k, d in zip(k_values, d_values)]
