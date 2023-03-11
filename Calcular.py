import MetaTrader5 as mt5

symbol = "EURUSD"
symbols = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF", "USDCAD", "NZDUSD", "EURJPY", "EURGBP", "EURCHF"]

#Fijo
risk=20

if not mt5.initialize():
    print("Hubo un error al iniciallizar la conexión, error code =",mt5.last_error())
    quit()


#TERMINADO
def calculate_optimal_lot(account_size, risk,point):
    # Convertimos el porcentaje de riesgo a decimal
    risk_decimal = risk / 100

    # Calculamos el tamaño de lote óptimo según el capital disponible en la cuenta y el porcentaje de riesgo
    optimal_lot = (account_size * risk_decimal) * point # Suponiendo que la divisa base es USD y 1 lote = 100000 unidades

    if optimal_lot < 0.01:
        optimal_lot=0.01

    return optimal_lot

#TERMINADO
def stoploss_takeprofit(priceask,pricebid, reward, type, pips):
    if type == mt5.ORDER_TYPE_BUY:
        stop_loss = priceask - (pips/100000)
        take_profit = priceask + (reward * pips)/100000
        return stop_loss, take_profit
    elif type == mt5.ORDER_TYPE_SELL:
        stop_loss = pricebid + pips/100000
        take_profit = pricebid - (reward * pips)/100000
        return stop_loss, take_profit

#TERMINADO
def order(symbol,type,price,lot,sl,tp,comment,deviation=20):

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
            "comment": comment,
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

def buy(symbol,str):
    priceask = mt5.symbol_info_tick(symbol).ask
    pricebid = mt5.symbol_info_tick(symbol).bid
    
    sl,tp = stoploss_takeprofit(priceask,pricebid, 2, mt5.ORDER_TYPE_BUY, 50)

    order(symbol,mt5.ORDER_TYPE_BUY,priceask,0.01,sl,tp,str,deviation=20)

def sell(symbol,str):
    priceask = mt5.symbol_info_tick(symbol).ask
    pricebid = mt5.symbol_info_tick(symbol).bid
    
    sl,tp = stoploss_takeprofit(priceask,pricebid, 2, mt5.ORDER_TYPE_SELL, 50)

    order(symbol,mt5.ORDER_TYPE_SELL,priceask,0.01,sl,tp,str,deviation=20)

def active(str):
    for order in mt5.orders_get():
        if order.comment == str:
            # Se ha encontrado la orden
            print("Existe una orden activa de esta estrategia")
            return False
    
    return True