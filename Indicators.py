import pandas_ta as ta

def calculate_rsi(df, period=14):
    """Calcula el RSI"""
    rsi = ta.rsi(df['close'], length=period)
    return rsi.iloc[-1]

def calculate_ma(df, period=50):
    """Calcula la Media Móvil"""
    ma = ta.sma(df['close'], length=period)
    return ma.iloc[-1]


















'''
def calculate_macd(df, fast_period=12, slow_period=26, signal_period=9):
    """Calcula el MACD"""
    macd = ta.macd(df['close'], fast=fast_period, slow=slow_period, signal=signal_period)
    return macd['MACD'].iloc[-1], macd['SIGNAL'].iloc[-1]

def calculate_bollinger_bands(df, period=20, deviation=2):
    """Calcula las Bandas de Bollinger"""
    bb = ta.bbands(df['close'], length=period, std=deviation)
    return bb['BBL_20_2.0'].iloc[-1], bb['BBM_20_2.0'].iloc[-1], bb['BBU_20_2.0'].iloc[-1]

def calculate_stochastic(df, k_period=14, d_period=3):
    """Calcula el Estocástico"""
    stoch = ta.stoch(df['high'], df['low'], df['close'], k=k_period, d=d_period)
    return stoch['STOCHk_14_3'].iloc[-1], stoch['STOCHd_14_3'].iloc[-1]
'''