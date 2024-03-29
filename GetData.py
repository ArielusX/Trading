import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.dates as mdates

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

# convertir el DataFrame en una lista de tuplas OHLC
ohlc = df[['open', 'high', 'low', 'close']].reset_index().values.tolist()
ohlc = [(mdates.date2num(date), open, high, low, close) for date, open, high, low, close in ohlc]

# trazar el gráfico de velas japonesas
fig, ax = plt.subplots()
mpl_finance.candlestick_ohlc(ax, ohlc, width=0.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.set_title('Gráfico de velas japonesas para EURUSD')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio')
plt.xticks(rotation=30)
plt.show()