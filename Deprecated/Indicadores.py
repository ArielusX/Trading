import MetaTrader5 as mt5
import talib
import numpy as np

def calculate_ma(symbol, timeframe, period, ma_type):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 10)
    close_prices = rates['close']
    ma = talib.MA(close_prices, timeperiod=period, matype=ma_type)
    return ma[-1]

def calculate_rsi(symbol, timeframe, period):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 10)
    close_prices = rates['close']
    rsi = talib.RSI(close_prices, timeperiod=period)
    return rsi[-1]

def calculate_macd(symbol, timeframe, fast_period, slow_period, signal_period):
    total_period = slow_period + signal_period + 10
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, total_period)
    close_prices = rates['close']
    macd, signal, _ = talib.MACD(close_prices, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
    return macd[-1], signal[-1]

def calculate_bollinger_bands(symbol, timeframe, period, deviation):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 10)
    close_prices = rates['close']
    upper, middle, lower = talib.BBANDS(close_prices, timeperiod=period, nbdevup=deviation, nbdevdn=deviation, matype=0)
    return upper[-1], middle[-1], lower[-1]

def calculate_ichimoku(symbol, timeframe):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
    highs = rates['high']
    lows = rates['low']
    closes = rates['close']
    tenkan_sen = talib.SMA(highs, timeperiod=9)
    kijun_sen = talib.SMA(lows, timeperiod=26)
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2)[:-26]
    senkou_span_b = talib.SMA(closes, timeperiod=52)[:-26]
    chikou_span = closes[:-26]
    return tenkan_sen[-1], kijun_sen[-1], senkou_span_a[-1], senkou_span_b[-1], chikou_span[-1]

def calculate_stochastic(symbol, timeframe, period, k_period, d_period):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 10)
    high = rates['high']
    low = rates['low']
    close = rates['close']
    slowk, slowd = talib.STOCH(high, low, close, fastk_period=k_period,
                               slowk_period=d_period, slowk_matype=0,
                               slowd_period=3, slowd_matype=0)
    return slowk[-1], slowd[-1]
