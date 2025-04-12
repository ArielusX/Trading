import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

def get_data(symbol, timeframe=mt5.TIMEFRAME_M5, n_bars=5000):

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_bars)

    if rates is None or len(rates) == 0:
        print("No se pudieron obtener datos del símbolo:", symbol)
        return None

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
