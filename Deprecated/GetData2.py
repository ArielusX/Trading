import MetaTrader5 as mt5

def get_price(symbol):
    """Obtiene el precio actual Ask del par de divisas"""
    tick = mt5.symbol_info_tick(symbol)
    return tick.ask

def get_data(symbol, timeframe, period):
    """Obtiene los datos históricos de MetaTrader 5"""
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 10)
    df = pd.DataFrame(rates)
    return df