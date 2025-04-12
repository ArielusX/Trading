import MetaTrader5 as mt5
import time
import Data as data  # Este es el módulo donde tienes la función get_data
import Operations as oper  # Este es el módulo donde tienes las funciones de comprar y vender
import Indicators as ind   # Este es el módulo donde tienes las funciones para calcular los indicadores (MA, RSI)
import Strategies as str
import Login as login
import Backtesting as test

def main():

    login.initialize()

    symbols = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF", "USDCAD", "NZDUSD", "EURJPY", "EURGBP", "EURCHF"]


    # Configuración de parámetros
    timeframe = mt5.TIMEFRAME_H1  # Marco temporal 
    ma_fast_period = 10  # Periodo de la MA rápida
    ma_slow_period = 50  # Periodo de la MA lenta
    rsi_period = 14  # Periodo del RSI
    rsi_buy_threshold = 45  # Umbral de compra para el RSI
    rsi_sell_threshold = 55  # Umbral de venta para el RSI

    # Ciclo principal para ejecutar la estrategia para cada símbolo
    try:
        while True:
            for symbol in symbols:
                # Ejecutar la estrategia de trading para cada símbolo
                #str.ma_rsi_strategy(symbol, timeframe, ma_fast_period, ma_slow_period, rsi_period, rsi_buy_threshold, rsi_sell_threshold)
                test.backtest_ma_rsi(symbol, timeframe, ma_fast_period, ma_slow_period, rsi_period, rsi_buy_threshold, rsi_sell_threshold)
                time.sleep(2)  # Espera un poco antes de pasar al siguiente símbolo (ajústalo si es necesario)
            
            # Esperar un período de tiempo antes de ejecutar la siguiente iteración para todos los símbolos
            time.sleep(600)  # Espera 60 segundos (puedes ajustarlo según tu necesidad)
    
    except KeyboardInterrupt:
        print("Ejecución interrumpida por el usuario.")
    
    finally:
        # Cerrar la conexión con MetaTrader 5 al finalizar el script
        mt5.shutdown()

if __name__ == "__main__":
    main()
