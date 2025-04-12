import MetaTrader5 as mt5
import pandas as pd

symbol = "EURUSD"
timeframe = 1  # 1 para M1 (1 minuto), puedes cambiarlo según tus necesidades

# Obtén datos históricos
history = mt5.copy_rates(symbol, timeframe, 0, 1000)

# Crea un DataFrame con los datos históricos
df = pd.DataFrame(history)
df['time'] = pd.to_datetime(df['time'], unit='s')  # Convierte el tiempo a formato de fecha y hora
df.set_index('time', inplace=True)

# Muestra el DataFrame con los datos
print(df)

# Desconéctate de MetaTrader5
mt5.logout()