


def open_trade(symbol, action, lot_size=0.1):
    """Abre una orden de compra o venta"""
    price = get_price(symbol)
    if action == 'buy':
        order = mt5.OrderSend(symbol, mt5.ORDER_TYPE_BUY, lot_size, price, 3, 0, 0, "Compra RSI y MA", 0, 0, mt5.COLOR_GREEN)
    elif action == 'sell':
        order = mt5.OrderSend(symbol, mt5.ORDER_TYPE_SELL, lot_size, price, 3, 0, 0, "Venta RSI y MA", 0, 0, mt5.COLOR_RED)
    if order < 0:
        print(f"Error al abrir la orden: {mt5.last_error()}")
    else:
        print(f"Orden {action} ejecutada a {price}")

def close_trade(symbol):
    """Cierra todas las posiciones abiertas"""
    positions = mt5.positions_get(symbol=symbol)
    for pos in positions:
        ticket = pos.ticket
        result = mt5.OrderSend(symbol, mt5.ORDER_TYPE_SELL, pos.volume, get_price(symbol), 3, 0, 0, "Cierre de orden", 0, 0, mt5.COLOR_RED)
        if result < 0:
            print(f"Error al cerrar la orden: {mt5.last_error()}")
        else:
            print(f"Posición cerrada con éxito")

def check_conditions(symbol, timeframe, rsi_period, ma_period):
    """Verifica las condiciones para abrir o cerrar una operación"""
    df = get_data(symbol, timeframe, rsi_period)
    rsi_value = calculate_rsi(df, rsi_period)
    ma_value = calculate_ma(df, ma_period)
    current_price = get_price(symbol)
    
    print(f"RSI: {rsi_value}, MA: {ma_value}, Precio actual: {current_price}")
    
    # Condición para comprar: RSI < 30 y el precio está por encima de la media móvil
    if rsi_value < 30 and current_price > ma_value:
        open_trade(symbol, 'buy')
    
    # Condición para vender: RSI > 70 y el precio está por debajo de la media móvil
    if rsi_value > 70 and current_price < ma_value:
        close_trade(symbol)

def main():
    symbol = "BTCUSD"
    timeframe = mt5.TIMEFRAME_M5  # 5 minutos
    rsi_period = 14
    ma_period = 50
    
    while True:
        check_conditions(symbol, timeframe, rsi_period, ma_period)
        time.sleep(60)  # Espera 1 minuto antes de revisar nuevamente

if __name__ == "__main__":
    main()


def open_trade(symbol, action, lot_size=0.1, sl_points=100, tp_points=200):
    """Abre una orden de compra o venta con SL y TP en puntos"""
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask if action == 'buy' else mt5.symbol_info_tick(symbol).bid

    if action == 'buy':
        sl = price - sl_points * point
        tp = price + tp_points * point
        order_type = mt5.ORDER_TYPE_BUY
        color = mt5.COLOR_GREEN
    elif action == 'sell':
        sl = price + sl_points * point
        tp = price - tp_points * point
        order_type = mt5.ORDER_TYPE_SELL
        color = mt5.COLOR_RED
    else:
        print("Acción no válida: debe ser 'buy' o 'sell'")
        return

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 234000,  # número mágico personalizado
        "comment": "Trade con SL y TP",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Error al abrir la orden: {result.retcode} - {result.comment}")
    else:
        print(f"✅ Orden {action.upper()} ejecutada en {price} con SL={sl}, TP={tp}")
