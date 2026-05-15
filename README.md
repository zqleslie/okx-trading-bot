# OKX Trading Bot

Automated cryptocurrency trading bot for OKX with built-in risk management.

## Features

- J-value auto-intercept (J>50)
- Price change auto-intercept (>7%)
- Kelly formula position sizing
- RSI/MACD/Bollinger Bands signals
- Backtesting framework

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set API keys in `.env`
3. Run: `python main.py`

## Risk Rules

- **Never margin trade**
- **Single position <= 30%**
- **Stop loss: -8%**
- **Only long, no short**
