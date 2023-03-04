import MetaTrader5 as mt5
import Main
import talib

def calculate_ma(symbol, timeframe, period, ma_type):
    # Obtenemos los datos históricos
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    # Obtenemos solo los precios de cierre
    close_prices = [x[4] for x in rates]
    # Calculamos la media móvil utilizando la biblioteca talib
    ma = talib.MA(close_prices, timeperiod=14, matype=ma_type)
    return ma[-1]

def calculate_rsi(symbol, timeframe, period):
    # Obtenemos los datos históricos
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    # Obtenemos solo los precios de cierre
    close_prices = [x[4] for x in rates]
    # Calculamos el RSI utilizando la biblioteca talib
    rsi = talib.RSI(close_prices, timeperiod=14)
    return rsi[-1]

def calculate_macd(symbol, timeframe, fast_period, slow_period, signal_period):
    # Obtenemos los datos históricos
    rates = mt5.copy_rates_from(symbol, timeframe, 0, fast_period + signal_period)
    # Obtenemos solo los precios de cierre
    close_prices = [x[4] for x in rates]
    # Calculamos el MACD utilizando la biblioteca talib
    macd, signal, _ = talib.MACD(close_prices, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
    return macd[-1], signal[-1]

def calculate_bollinger_bands(symbol, timeframe, period, deviation):
    # Obtener datos históricos
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    # Obtener precios de cierre
    close_prices = [x[4] for x in rates]
    # Calcular las bandas de Bollinger utilizando la biblioteca talib
    upper_band, middle_band, lower_band = talib.BBANDS(close_prices, timeperiod=20, nbdevup=deviation, nbdevdn=deviation, matype=0)
    return upper_band[-1], middle_band[-1], lower_band[-1]


def calculate_hichimoku(symbol, timeframe):
    # Obtenemos los datos del par de divisas y el período de tiempo
    rates = mt5.copy_rates_from(symbol, timeframe, 0, 26)
    # Extraemos los precios de apertura, cierre, máximo y mínimo de cada barra
    opens = [x['open'] for x in rates]
    closes = [x['close'] for x in rates]
    highs = [x['high'] for x in rates]
    lows = [x['low'] for x in rates]
    # Calculamos los valores del indicador Hichimoku usando la función de la biblioteca TA-Lib
    tenkan_sen = talib.SMA(highs, timeperiod=9)
    kijun_sen = talib.SMA(lows, timeperiod=26)
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2)[:-26]
    senkou_span_b = talib.SMA(closes, timeperiod=52)[:-26]
    chikou_span = closes[:-26]
    return tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span

def calculate_stochastic(symbol, timeframe, period, k_period, d_period):
    # Obtener datos históricos
    rates = mt5.copy_rates_from(symbol, timeframe, 0, period)
    # Obtener precios de alta, baja y cierre
    high_prices = [x[2] for x in rates]
    low_prices = [x[3] for x in rates]
    close_prices = [x[4] for x in rates]
    # Calcular el estocástico utilizando la biblioteca talib
    slowk, slowd = talib.STOCH(high_prices, low_prices, close_prices, fastk_period=k_period, slowk_period=d_period, slowk_matype=0, slowd_period=3, slowd_matype=0)
    return slowk[-1], slowd[-1]