import time
import MetaTrader5 as mt5
 
# establecemos la conexión con el terminal MetaTrader 5
if not mt5.initialize():
    print("Hubo un error al iniciallizar la conexión, error code =",mt5.last_error())
    quit()
 

symbol = "USDJPY"
lot = 0.01

deviation = 20


symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()
