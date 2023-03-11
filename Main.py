import time
import MetaTrader5 as mt5
import Calcular as cal
import Strategies as str

while True:
  
    if not mt5.initialize():
        print("Hubo un error al iniciallizar la conexión, error code =",mt5.last_error())
        quit()

    symbol = "EURUSD"
    symbols = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF", "USDCAD", "NZDUSD", "EURJPY", "EURGBP", "EURCHF"]

    for symbol in symbols:
        print('ma_rsi',symbol)
        if cal.active("ma_rsi"+symbol):
            str.ma_rsi_strategy(symbol)
 

    time.sleep(10)
    
   
   


