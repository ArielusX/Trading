import MetaTrader5 as mt5
import pandas as pd

# inicializar conexión con MetaTrader 5
mt5.initialize()

# copiar datos históricos de precios de EURUSD en el marco de tiempo D1
symbol = 'EURUSD'
timeframe = mt5.TIMEFRAME_D1
start_pos = 0
count = 1000
rates = mt5.copy_rates_from_pos(symbol, timeframe, start_pos, count)

# crear un DataFrame de pandas a partir de los datos históricos
df = pd.DataFrame(rates)

# establecer el índice del DataFrame como la fecha y hora del precio
df['time'] = pd.to_datetime(df['time'], unit='s')
df.set_index('time', inplace=True)

# cerrar conexión con MetaTrader 5
mt5.shutdown()

# imprimir el DataFrame
print(df.head())