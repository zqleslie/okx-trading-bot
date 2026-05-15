"""Risk management module."""


def kelly_position(win_rate: float, avg_win: float, avg_loss: float) -> float:
    """Calculate Kelly criterion position size, capped at 30%."""
    if avg_loss == 0:
        return 0.0
    b = avg_win / avg_loss
    kelly = (b * win_rate - (1 - win_rate)) / b
    return max(0.0, min(kelly, 0.3))


def check_price_intercept(entry_price: float, current_price: float) -> dict:
    """Check if price change triggers auto-intercept rules."""
    change_pct = ((current_price - entry_price) / entry_price) * 100
    if change_pct > 7:
        return {"action": "INTERCEPT", "reason": "Price change > 7%"}
    if change_pct < -8:
        return {"action": "STOP_LOSS", "reason": "Stop loss triggered (-8%)"}
    return {"action": "HOLD", "reason": "Within normal range"}
