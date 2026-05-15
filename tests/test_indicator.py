"""Unit tests for technical indicators."""
import pytest
from signals.indicator import calculate_rsi, calculate_j


def test_rsi_oversold():
    prices = list(range(100, 50, -1))
    rsi = calculate_rsi(prices)
    assert rsi < 30, f"RSI should be <30 for falling prices, got {rsi}"


def test_rsi_overbought():
    prices = list(range(50, 100))
    rsi = calculate_rsi(prices)
    assert rsi > 70, f"RSI should be >70 for rising prices, got {rsi}"


def test_j_value():
    k = [50, 55, 60, 65, 70]
    d = [45, 48, 52, 56, 61]
    j = calculate_j(k, d)
    assert len(j) == 5
