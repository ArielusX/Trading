import MetaTrader5 as mt5
import Indicators as ind
import Operations as oper
import Data as data

def ma_rsi_strategy(symbol, timeframe = mt5.TIMEFRAME_M5, ma_fast_period=10, ma_slow_period=50, rsi_period=14, rsi_buy_threshold=30, rsi_sell_threshold=70):
    # Obtener precios de cierre
    close_prices = data.get_data(symbol, timeframe, ma_slow_period)

    # Calcular MA rápida y lenta
    ma_fast = ind.calculate_ma(close_prices, ma_fast_period)
    ma_slow = ind.calculate_ma(close_prices, ma_slow_period)

    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    # Realizar operaciones en función de las señales
    if ma_fast > ma_slow and rsi < rsi_buy_threshold:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        oper.buy(symbol,"ma_rsi")
    elif ma_fast < ma_slow and rsi > rsi_sell_threshold:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        oper.sell(symbol,"ma_rsi")
    else:
        print("No se ha enviado ninguna señal para {} con la estrategia de medias moviles y RSI".format(symbol))
