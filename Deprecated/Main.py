import time
import MetaTrader5 as mt5
import Calcular as cal
import Strategies as str
import Deprecated.IndicadoresS as ind

while True:
  
    if not mt5.initialize():
        print("Hubo un error al iniciallizar la conexión, error code =",mt5.last_error())
        quit()

    symbol = "EURUSD"
    symbols = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF", "USDCAD", "NZDUSD", "EURJPY", "EURGBP", "EURCHF"]

    for symbol in symbols:
        print('ma_rsi',symbol)
       # if cal.active("ma_rsi"+symbol):
           # str.ma_rsi_strategy(symbol)

    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_M5
    rsi_period = 14

    close_prices = ind.get_close_prices(symbol, timeframe, rsi_period)
    str.plot_rsi(close_prices, rsi_period)
 

    time.sleep(10)
    
   
   


