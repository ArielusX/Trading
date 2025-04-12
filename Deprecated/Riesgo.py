import math
import MetaTrader5 as mt5
import pandas as pd

# Establecer conexión con la terminal
if not mt5.initialize():
    print("ERROR")
    quit()

'''def calculate_optimal_lot(win_rate, reward_risk, account_size,max_risk):
    # Convertimos la tasa de acierto y la relación riesgo/beneficio a decimales
    win_rate = win_rate / 100
    reward_risk = reward_risk / 100

    # Calculamos la probabilidad de perder (lose_rate) y la expectativa matemática (expectancy)
    lose_rate = 1 - win_rate
    expectancy = (win_rate * reward_risk) - lose_rate

    # Calculamos el porcentaje óptimo de capital a arriesgar (optimal_fraction) según la fórmula de Kelly
    optimal_fraction = expectancy / reward_risk
    optimal_fraction = min(max(optimal_fraction, 0), 1)  # Limitamos el resultado entre 0 y 1
    optimal_fraction = min(optimal_fraction, max_risk/100)  # Limitamos el riesgo máximo al 2%

    # Calculamos el tamaño de lote óptimo (optimal_lot) según el capital disponible en la cuenta
    balance = account_size * optimal_fraction
    optimal_lot = balance / 100000  # Suponiendo que la divisa base es USD y 1 lote = 100000 unidades
    optimal_lot = max(optimal_lot, 0.01)  # Establecemos un tamaño mínimo de lote de 0.01

    return optimal_lot'''



def calculate_fixed_lot(symbol,balance, risk_percent, stop_loss_pips):
    # Convertimos el porcentaje de riesgo a decimal
    risk_decimal = risk_percent / 100
    
    # Calculamos el valor monetario del riesgo máximo permitido en la operación
    risk_money = balance * risk_decimal
    
    # Calculamos el tamaño del lote que corresponde para una operación con ese riesgo máximo
    point_value = mt5.symbol_info(symbol).point 
    print(point_value)
    lot_size = risk_money / (stop_loss_pips * point_value)
    
    return lot_size

symbol = "USDJPY"

symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask

def calculate_optimal_lot(account_size, risk_percentage):
    # Convertimos el porcentaje de riesgo a decimal
    risk_decimal = risk_percentage / 100

    # Calculamos el tamaño de lote óptimo según el capital disponible en la cuenta y el porcentaje de riesgo
    optimal_lot = (account_size * risk_decimal) * point # Suponiendo que la divisa base es USD y 1 lote = 100000 unidades

    return optimal_lot

win_rate = 60
reward_risk = 1
account_size = 1000
max_risk = 2
stop_loss_pips=100
symbol = "USDJPY"

#optimal_lot = calculate_optimal_lot(win_rate, reward_risk, account_size,max_risk)
optimal_lot = calculate_optimal_lot(account_size, max_risk)
lot_size = calculate_fixed_lot(symbol,account_size, max_risk, stop_loss_pips)

print("El tamano de lote optimo es:", "{:.2f}".format(optimal_lot))
print("El tamano de lote optimo es:", "{:.2f}".format(lot_size))