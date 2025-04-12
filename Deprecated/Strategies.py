import MetaTrader5 as mt5
import Deprecated.IndicadoresS as ind
import numpy as np
import Calcular as cal
import matplotlib.pyplot as plt



def ma_rsi_strategy(symbol, timeframe = mt5.TIMEFRAME_M5, ma_fast_period=10, ma_slow_period=50, rsi_period=14, rsi_buy_threshold=30, rsi_sell_threshold=70):
    # Obtener precios de cierre
    close_prices = ind.get_close_prices(symbol, timeframe, ma_slow_period)

    # Calcular MA rápida y lenta
    ma_fast = ind.calculate_ma(close_prices, ma_fast_period)
    ma_slow = ind.calculate_ma(close_prices, ma_slow_period)

    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    # Realizar operaciones en función de las señales
    if ma_fast > ma_slow and rsi < rsi_buy_threshold:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol,"ma_rsi")
    elif ma_fast < ma_slow and rsi > rsi_sell_threshold:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol,"ma_rsi")

def plot_rsi(close_prices, rsi_period):
    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    if rsi is None:
        print("No se pudo trazar el gráfico de RSI")
        return

    # Crear un array de índices de tiempo para el gráfico
    x = range(len(rsi))

    # Crear el gráfico de RSI
    plt.plot(x, rsi)
    plt.xlabel('Time')
    plt.ylabel('RSI')
    plt.title('RSI Chart')
    plt.show()


def ma_rsi_macd_strategy(symbol, timeframe, ma_fast_period, ma_slow_period, rsi_period, rsi_buy_threshold, rsi_sell_threshold, macd_fast_period, macd_slow_period, macd_signal_period):
    # Obtener precios de cierre
    close_prices = ind.get_close_prices(symbol, timeframe, ma_slow_period)

    # Calcular MA rápida y lenta
    ma_fast = ind.calculate_ma(close_prices, ma_fast_period)
    ma_slow = ind.calculate_ma(close_prices, ma_slow_period)

    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    # Calcular MACD
    macd, signal = ind.calculate_macd(close_prices, macd_fast_period, macd_slow_period, macd_signal_period)

    # Realizar operaciones en función de las señales
    if ma_fast > ma_slow and rsi < rsi_buy_threshold and macd > signal:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol)
    elif ma_fast < ma_slow and rsi > rsi_sell_threshold and macd < signal:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol)

def ichimoku_stochastic_strategy(symbol, timeframe, k_period, d_period, tenkan_period, kijun_period, senkou_period):
    # Obtener precios de cierre, altos y bajos
    close_prices = ind.get_close_prices(symbol, timeframe, senkou_period)
    high_prices = mt5.copy_rates_from(symbol, timeframe, 0, senkou_period)['high']
    low_prices = mt5.copy_rates_from(symbol, timeframe, 0, senkou_period)['low']

    # Calcular Ichimoku Cloud
    tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span = ind.calculate_hichimoku(high_prices, low_prices, close_prices)

    # Calcular Stochastic
    slowk, slowd = ind.calculate_stochastic(high_prices, low_prices, close_prices, k_period, d_period)

    # Realizar operaciones en función de las señales
    if close_prices[-1] > senkou_span_a[-1] and close_prices[-1] > senkou_span_b[-1] and tenkan_sen[-1] > kijun_sen[-1] and slowk > slowd:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol)
    elif close_prices[-1] < senkou_span_a[-1] and close_prices[-1] < senkou_span_b[-1] and tenkan_sen[-1] < kijun_sen[-1] and slowk < slowd:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol)

def ichimoku_rsi_macd_strategy(symbol, timeframe, rsi_period, rsi_buy_threshold, rsi_sell_threshold, macd_fast_period, macd_slow_period, macd_signal_period):
    # Obtener precios de alta, baja y cierre
    high_prices = np.array(mt5.copy_rates_from_pos(symbol, timeframe, 0, 135)['high'])
    low_prices = np.array(mt5.copy_rates_from_pos(symbol, timeframe, 0, 135)['low'])
    close_prices = np.array(mt5.copy_rates_from_pos(symbol, timeframe, 0, 135)['close'])

    # Calcular Ichimoku
    tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span = ind.calculate_hichimoku(high_prices, low_prices, close_prices)

    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    # Calcular MACD
    macd, signal = ind.calculate_macd(close_prices, macd_fast_period, macd_slow_period, macd_signal_period)

    # Realizar operaciones en función de las señales
    if tenkan_sen[-1] > kijun_sen[-1] and close_prices[-1] > senkou_span_a[-1] and close_prices[-1] > senkou_span_b[-1] and rsi < rsi_buy_threshold and macd > signal:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol)
    elif tenkan_sen[-1] < kijun_sen[-1] and close_prices[-1] < senkou_span_a[-1] and close_prices[-1] < senkou_span_b[-1] and rsi > rsi_sell_threshold and macd < signal:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol)

def ma_rsi_stoch_strategy(symbol, timeframe, ma_fast_period, ma_slow_period, rsi_period, rsi_buy_threshold, rsi_sell_threshold, stoch_k_period, stoch_d_period, stoch_slowing_period):
    # Obtener precios de cierre
    close_prices = ind.get_close_prices(symbol, timeframe, ma_slow_period)

    # Calcular MA rápida y lenta
    ma_fast = ind.calculate_ma(close_prices, ma_fast_period)
    ma_slow = ind.calculate_ma(close_prices, ma_slow_period)

    # Calcular RSI
    rsi = ind.calculate_rsi(close_prices, rsi_period)

    # Calcular Stochastic
    stoch_k, stoch_d = ind.calculate_stochastic(close_prices, stoch_k_period, stoch_d_period, stoch_slowing_period)

    # Realizar operaciones en función de las señales
    if ma_fast[-1] > ma_slow[-1] and rsi[-1] < rsi_buy_threshold and stoch_k[-1] < stoch_d[-1]:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol)
    elif ma_fast[-1] < ma_slow[-1] and rsi[-1] > rsi_sell_threshold and stoch_k[-1] > stoch_d[-1]:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol)

def ma_macd_strategy(symbol, timeframe, ma_fast_period, ma_slow_period, macd_fast_period, macd_slow_period, macd_signal_period):
    # Obtener precios de cierre
    close_prices = ind.get_close_prices(symbol, timeframe, ma_slow_period)

    # Calcular MA rápida y lenta
    ma_fast = ind.calculate_ma(close_prices, ma_fast_period)
    ma_slow = ind.calculate_ma(close_prices, ma_slow_period)

    # Calcular MACD
    macd, macd_signal, _ = ind.calculate_macd(close_prices, macd_fast_period, macd_slow_period, macd_signal_period)

    # Realizar operaciones en función de las señales
    if ma_fast[-1] > ma_slow[-1] and macd[-1] > macd_signal[-1]:
        print(f'Buy signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.buy(symbol)
    elif ma_fast[-1] < ma_slow[-1] and macd[-1] < macd_signal[-1]:
        print(f'Sell signal for {symbol} at {mt5.symbol_info_tick(symbol).bid}')
        cal.sell(symbol)









'''

def hichimoku_strategy(symbol, tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span):
    # Comprobamos si el precio actual está por encima o por debajo del kijun_sen
    if price > kijun_sen[-1]:
        # Comprobamos si el precio está por encima o por debajo de la nube
        if price > senkou_span_a[-1] and price > senkou_span_b[-1]:
            # Si el precio está por encima de la nube y el tenkan_sen está por encima del kijun_sen, abrimos una posición larga
            if tenkan_sen[-1] > kijun_sen[-1]:
                sl = kijun_sen[-1]
                tp = senkou_span_b[-1]
                # Abrimos la posición larga
               
                print("Posición larga abierta: Operación de compra de {} lotes del par {} a {} con SL en {} y TP en {}".format(lot, symbol, price, sl, tp))
                return True
    # Si el precio está por debajo del kijun_sen, comprobamos si está por debajo de la nube y si el tenkan_sen está por debajo del kijun_sen
    elif price < kijun_sen[-1]:
        if price < senkou_span_a[-1] and price < senkou_span_b[-1]:
            if tenkan_sen[-1] < kijun_sen[-1]:
                sl = kijun_sen[-1]
                tp = senkou_span_b[-1]
                # Abrimos la posición corta
               
                print("Posición corta abierta: Operación de venta de {} lotes del par {} a {} con SL en {} y TP en {}".format(lot, symbol, price, sl, tp))
                return True
    return False

# Definimos la estrategia basada en el RSI
def rsi_strategy(symbol):
    # Calculamos el RSI
    rsi = ind.calculate_rsi(symbol, 14)
    # Si el RSI es menor que 30, abrimos una posición de compra
    if rsi < 30:
        Main.order(symbol, mt5.ORDER_TYPE_BUY, price, lot, deviation, stoploss(point, price, risk, type), takeprofit(point, price, risk, type))
    # Si el RSI es mayor que 70, abrimos una posición de venta
    elif rsi > 70:
        Main.order(symbol, mt5.ORDER_TYPE_SELL, price, lot, deviation, stoploss(point, price, risk, type), takeprofit(point, price, risk, type))

'''