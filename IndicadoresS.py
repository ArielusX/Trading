import MetaTrader5 as mt5
import numpy as np
import pandas_ta as ta

def get_close_prices(symbol, timeframe, period):
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    return [x[4] for x in rates]

def calculate_ma(close_prices, period, ma_type='SMA'):
    return ta.trend.ema(close_prices, length=period)[-1] if ma_type == 'EMA' else np.mean(close_prices[-period:])

def calculate_rsi(close_prices, period):
    return ta.momentum.rsi(close_prices, length=period)[-1]

def calculate_macd(close_prices, fast_period, slow_period, signal_period):
    macd = ta.trend.macd(close_prices, fast=fast_period, slow=slow_period, signal=signal_period)['MACD'].iloc[-1]
    signal = ta.trend.macd(close_prices, fast=fast_period, slow=slow_period, signal=signal_period)['SIGNAL'].iloc[-1]
    return macd, signal

def calculate_bollinger_bands(close_prices, period, deviation):
    upper_band = ta.volatility.bollinger_hband(close_prices, length=period, std=deviation)[-1]
    middle_band = ta.volatility.bollinger_mavg(close_prices, length=period)[-1]
    lower_band = ta.volatility.bollinger_lband(close_prices, length=period, std=deviation)[-1]
    return upper_band, middle_band, lower_band

def calculate_stochastic(high_prices, low_prices, close_prices, k_period, d_period):
    k = ta.momentum.stoch(high_prices, low_prices, close_prices, k=k_period, d=d_period)['STOCH'].iloc[-1]
    d = ta.momentum.stoch(high_prices, low_prices, close_prices, k=k_period, d=d_period)['STOCHD'].iloc[-1]
    return k, d