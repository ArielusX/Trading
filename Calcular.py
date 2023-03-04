import MetaTrader5 as mt5
import Main

symbol = "USDJPY"
lot = 0.01
type =mt5.ORDER_TYPE_BUY
deviation = 20
risk=100;


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
        return price - (risk) * point;


def order(symbol,type,price,lot,deviation,sl,tp):
    
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        result = mt5.order_send(request)

        if type==mt5.ORDER_TYPE_BUY :
            operation = "Compra"
        elif type==mt5.ORDER_TYPE_SELL:
            operation = "Venta"
        else :
            operation = "desconocida"
        

        print("Orden enviada: Operacion de {} del par {} de {} lotes".format(operation,symbol,lot));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("La orden ha fallado. CODIGO DE ERROR: retcode={}".format(result.retcode))
            mt5.shutdown()
            quit()
        
        print("Orden ejecutada correctamente")
        # finalizamos la conexión con el terminal MetaTrader 5
        mt5.shutdown()