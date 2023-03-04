import time
import MetaTrader5 as mt5
import talib

while True:
  
    if not mt5.initialize():
        print("Hubo un error al iniciallizar la conexión, error code =",mt5.last_error())
        quit()

        

symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask

def stoploss(point,price,risk,type):
    if type==mt5.ORDER_TYPE_BUY :
        return price - (risk) * point;
    elif type==mt5.ORDER_TYPE_SELL:
        return price + (risk) * point;


def takeprofit(point,price,risk,type):
    if type==mt5.ORDER_TYPE_BUY :
        return price + risk * point;
    elif type==mt5.ORDER_TYPE_SELL:
        return price - (risk) * point;s
    

    time.sleep(10)
    
   
   


