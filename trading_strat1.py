''' Applies a dual moving average crossover strategy to historical stock price data '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv('Apple.csv')

# Sorts the data in case they are in reverse chronological order
data = data.iloc[::-1]
data = data.reset_index()

# Calculates the short (30-day) and long (100-day) averages
data30 = pd.DataFrame()
data30['Adj Close'] = data['Adj Close'].rolling(window=30).mean()
data100 = pd.DataFrame()
data100['Adj Close'] = data['Adj Close'].rolling(window=100).mean()

# Define a new data frame to implement ths strategy:
new = pd.DataFrame()
new['Adj Close'] = data['Adj Close']
new['data30'] = data30['Adj Close']
new['data100'] = data100['Adj Close']
# We find the crossing points by looking at the difference between the short and long averages:
new['diff'] = data30['Adj Close'] - data100['Adj Close']

# Main function. It identifies where the difference changes sign and stores
# the corresponding buy/sell price values. At points where there's on crossing,
# it appends NaN (to avoid inconsistencies with object's lenght)
def fun(dat):
    c = []
    buy, sell = [np.nan], [np.nan]
    for i in range(1, len(dat)):
        if (dat['diff'][i-1] > 0 and dat['diff'][i] < 0):
            sell.append(dat['Adj Close'][i])
            buy.append(np.nan)
            c.append(dat['Adj Close'][i])
        elif (dat['diff'][i-1] < 0 and dat['diff'][i] > 0):
            buy.append(dat['Adj Close'][i])
            sell.append(np.nan)
            c.append(-dat['Adj Close'][i])
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    return buy, sell, c

# Add two columns to the new data frame: buy and sell prices obtained from the function
buy_sell = fun(new)
new['Buy Price'] = buy_sell[0]
new['Sell Price'] = buy_sell[1]

# Plot everything
plt.figure(figsize=(12.5, 7.5))
plt.plot(data['Adj Close'], label = 'Data')
plt.plot(data30['Adj Close'], label = 'Short-term average')
plt.plot(data100['Adj Close'], label = 'Long-term average')
plt.scatter(new.index, new['Buy Price'], marker = '^', color = 'green', label='Buy')
plt.scatter(new.index, new['Sell Price'], marker = 'v', color = 'red', label = 'Sell')
plt.legend(loc = 'upper left')
plt.xlabel('Time (days)')
plt.ylabel('Stock price')
plt.show()
