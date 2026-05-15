"""Backtesting framework."""
from signals.engine import generate_signal
from risk.manager import kelly_position


def run_backtest(data: list[dict], initial_capital: float = 10000) -> dict:
    """Run backtest on historical data."""
    capital = initial_capital
    positions = []
    for i in range(20, len(data)):
        prices = [d["close"] for d in data[max(0, i - 20) : i + 1]]
        signal = generate_signal(prices, data[i]["k"], data[i]["d"])
        if signal["signal"] == "BUY":
            position_size = kelly_position(0.55, 0.05, 0.08)
            positions.append({"entry": data[i]["close"], "size": position_size})
    return {"capital": capital, "positions": positions}
