import MetaTrader5 as mt5

def buy(symbol, strategy, lot_size=0.1, sl_points=100, tp_points=200):
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    sl = price - sl_points * point
    tp = price + tp_points * point

    result = mt5.order_send(
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot_size,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 10,
            "magic": 100000,
            "comment": f"Buy {strategy}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
    )
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Error BUY {symbol}: {result.retcode}, {mt5.last_error()}")
    else:
        print(f"BUY {symbol} @ {price} | Strategy: {strategy}")
        print(f"Orden {symbol} ejecutada a {price}")

def sell(symbol, strategy, lot_size=0.1, sl_points=100, tp_points=200):
    #Revisar proporcion 1:2
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).bid
    sl = price + sl_points * point
    tp = price - tp_points * point

    result = mt5.order_send(
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot_size,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 10,
            "magic": 100000,
            "comment": f"Buy {strategy}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
    )
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Error SELL {symbol}: {result.retcode}, {mt5.last_error()}")
    else:
        print(f"SELL {symbol} @ {price} | Strategy: {strategy}")
