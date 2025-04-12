import pandas as pd

df = pd.read_csv("BTCUSDT.csv")
# get the last 30 prices
last_30_prices = df["Close"].tail(360)
# calculate the average of the last 30 prices
mean_price = last_30_prices.mean()
# calculate the standard deviation of prices
std_price = last_30_prices.std()
# calculating support and resistance levels
support_price = mean_price - std_price
resistance_price = mean_price + std_price
# last price data
last_price = df["Close"].iloc[-1]
# comparar el último precio con los niveles de soporte y resistencia
if last_price > resistance_price:
    status = "resistance"
    difference = last_price - resistance_price
elif last_price < support_price:
    status = "support"
    difference = support_price - last_price
else:
    status = "neutral"
    difference = 0
# 
print(f"The last price ({last_price}) is {status} with the difference {difference}.")
if status=="resistance":
    print("Send order to Sell")
elif status=="support":
    print("Send order Buy")
else:
    print("Hold/Or nothing")

