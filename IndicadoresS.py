import MetaTrader5 as mt5
import talib

def get_close_prices(symbol, timeframe, period):
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    return [x[4] for x in rates]

def calculate_ma(close_prices, period, ma_type):
    return talib.MA(close_prices, timeperiod=period, matype=ma_type)[-1]

def calculate_rsi(close_prices, period):
    return talib.RSI(close_prices, timeperiod=period)[-1]

def calculate_macd(close_prices, fast_period, slow_period, signal_period):
    macd, signal, _ = talib.MACD(close_prices, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
    return macd[-1], signal[-1]

def calculate_bollinger_bands(close_prices, period, deviation):
    upper_band, middle_band, lower_band = talib.BBANDS(close_prices, timeperiod=20, nbdevup=deviation, nbdevdn=deviation, matype=0)
    return upper_band[-1], middle_band[-1], lower_band[-1]

def calculate_hichimoku(high_prices, low_prices, close_prices):
    tenkan_sen = talib.SMA(high_prices, timeperiod=9)
    kijun_sen = talib.SMA(low_prices, timeperiod=26)
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2)[:-26]
    senkou_span_b = talib.SMA(close_prices, timeperiod=52)[:-26]
    chikou_span = close_prices[:-26]
    return tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span

def calculate_stochastic(high_prices, low_prices, close_prices, k_period, d_period):
    slowk, slowd = talib.STOCH(high_prices, low_prices, close_prices, fastk_period=k_period, slowk_period=d_period, slowk_matype=0, slowd_period=3, slowd_matype=0)
    return slowk[-1], slowd[-1]