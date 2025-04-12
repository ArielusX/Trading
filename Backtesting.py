import pandas as pd
import pandas_ta as ta
import MetaTrader5 as mt5
import time
import Data as data  # Este es el módulo donde tienes la función get_data
import Operations as oper  # Este es el módulo donde tienes las funciones de comprar y vender
import Indicators as ind   # Este es el módulo donde tienes las funciones para calcular los indicadores (MA, RSI)
import Strategies as str
import Login as login
import matplotlib.pyplot as plt 

def backtest_ma_rsi(symbol, timeframe=mt5.TIMEFRAME_M5, ma_fast_period=10, ma_slow_period=50, rsi_period=14, rsi_buy_threshold=30, rsi_sell_threshold=70, initial_balance=10000):
    # Obtener precios de cierre
    df = data.get_data(symbol, timeframe)
    if df is None:
        print(f"No se pudieron obtener datos para {symbol}")
        return None

    # Inicializar variables
    balance = initial_balance  # Saldo inicial
    position = 0  # 0 significa sin posición, 1 significa que estamos en una posición larga
    buy_price = 0  # Precio de compra
    total_trades = 0  # Contador de operaciones realizadas
    profits = []  # Lista de ganancias de cada operación

    # Realizar el backtest
    for i in range(0, len(df)):
        row = df.iloc[i]

        # Calculamos los indicadores
        ma_fast = ind.calculate_ma(df, ma_fast_period)
        ma_slow = ind.calculate_ma(df, ma_slow_period)
        rsi = ind.calculate_rsi(df, rsi_period)

        print(ma_fast)
        print(ma_slow)
        print(rsi)

        # Verifica si hay una señal de compra
        if ma_fast > ma_slow and rsi < rsi_buy_threshold and position == 0:
            # Comprar (entrar en la posición)
            position = 1
            buy_price = row['close']
            print(f"Señal de compra en {df.index[i]} - Precio: {buy_price}")
        
        # Verifica si hay una señal de venta
        elif ma_fast < ma_slow and rsi > rsi_sell_threshold and position == 1:
            # Vender (cerrar la posición)
            sell_price = row['close']
            profit = sell_price - buy_price  # Ganancia de la operación
            balance += profit  # Actualizar el saldo
            profits.append(profit)  # Registrar la ganancia
            position = 0  # Cerrar la posición
            total_trades += 1  # Aumentar el número de operaciones realizadas
            print(f"Señal de venta en {df.index[i]} - Precio: {sell_price}, Ganancia: {profit}")

    # Resumen del rendimiento
    total_profit = balance - initial_balance  # Ganancia total
    win_rate = sum([1 for p in profits if p > 0]) / total_trades if total_trades > 0 else 0
    avg_profit = sum(profits) / total_trades if total_trades > 0 else 0
    max_drawdown = calculate_max_drawdown(profits)

    print(f"Rendimiento Total: {total_profit}")
    print(f"Porcentaje de operaciones ganadoras: {win_rate * 100}%")
    print(f"Ganancia promedio por operación: {avg_profit}")
    print(f"Drawdown máximo: {max_drawdown}")

    #plot_performance(df.index[ma_slow_period:], balance)

    return {
        "total_profit": total_profit,
        "win_rate": win_rate,
        "avg_profit": avg_profit,
        "max_drawdown": max_drawdown
    }

def calculate_max_drawdown(profits):
    # Calcula el drawdown máximo en una lista de ganancias
    cumulative_returns = pd.Series(profits, dtype='float64').cumsum()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown

'''
def plot_performance(dates, balances):
    """Graficar el rendimiento acumulado y el drawdown"""
    # Calcular el drawdown
    cumulative_returns = pd.Series(balances).cumsum()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak

    if len(dates) > 0 and len(cumulative_returns) > 0:
        # Crear la figura y el gráfico
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))

        # Graficar el rendimiento acumulado
        ax[0].plot(dates, cumulative_returns, label='Balance Acumulado', color='blue')
        ax[0].set_title('Rendimiento Acumulado')
        ax[0].set_xlabel('Fecha')
        ax[0].set_ylabel('Balance')
        ax[0].legend()

        # Graficar el drawdown
        ax[1].plot(dates, drawdown, label='Drawdown', color='red')
        ax[1].set_title('Drawdown')
        ax[1].set_xlabel('Fecha')
        ax[1].set_ylabel('Drawdown')
        ax[1].legend()

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()
    else:
        print("No hay datos suficientes para graficar.")

def plot_performance(dates, cumulative_returns):
    # Verifica que haya datos para graficar
    if len(dates) > 0 and len(cumulative_returns) > 0:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(dates, cumulative_returns, label='Balance Acumulado', color='blue')
        ax.set_title('Rendimiento del Backtest')
        ax.set_xlabel('Fecha')
        ax.set_ylabel('Balance Acumulado')
        ax.legend()
        plt.show()
'''