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
count = 500
rates = mt5.copy_rates_from_pos(symbol, timeframe, start_pos, count)

# crear un DataFrame de pandas a partir de los datos históricos
df = pd.DataFrame(rates)

# establecer el índice del DataFrame como la fecha y hora del precio
df['time'] = pd.to_datetime(df['time'], unit='s')
df.set_index('time', inplace=True)

# cerrar conexión con MetaTrader 5
mt5.shutdown()

# calcular las medias móviles exponenciales de 10, 20, 50 y 100 días
df['EMA10'] = df['close'].ewm(span=10, adjust=False).mean()
df['EMA20'] = df['close'].ewm(span=20, adjust=False).mean()
df['EMA50'] = df['close'].ewm(span=50, adjust=False).mean()
df['EMA100'] = df['close'].ewm(span=100, adjust=False).mean()

# convertir el DataFrame en una lista de tuplas OHLC
ohlc = df[['open', 'high', 'low', 'close']].reset_index().values.tolist()
ohlc = [(mdates.date2num(date), open, high, low, close) for date, open, high, low, close in ohlc]

# convertir el DataFrame de las medias móviles en una lista de tuplas (fecha, valor)
ema10 = df['EMA10'].reset_index().values.tolist()
ema10 = [(mdates.date2num(date), value) for date, value in ema10]

ema20 = df['EMA20'].reset_index().values.tolist()
ema20 = [(mdates.date2num(date), value) for date, value in ema20]

ema50 = df['EMA50'].reset_index().values.tolist()
ema50 = [(mdates.date2num(date), value) for date, value in ema50]

ema100 = df['EMA100'].reset_index().values.tolist()
ema100 = [(mdates.date2num(date), value) for date, value in ema100]

# trazar el gráfico de velas japonesas
fig, ax = plt.subplots()
mpl_finance.candlestick_ohlc(ax, ohlc, width=0.3, colorup='green', colordown='red')

# trazar las medias móviles exponenciales
ax.plot(*zip(*ema10), color='blue', label='EMA10')
ax.plot(*zip(*ema20), color='orange', label='EMA20')
ax.plot(*zip(*ema50), color='green', label='EMA50')
ax.plot(*zip(*ema100), color='red', label='EMA100')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.set_title('Gráfico de velas japonesas para EURUSD')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio')
ax.legend()
plt.xticks(rotation=30)
plt.show()
