Overview
This project implements a simple trading strategy based on the Exponential Moving Average (EMA) crossover. The script downloads historical stock data, calculates EMAs, generates buy/sell signals, and evaluates the performance of the strategy with various metrics.

Requirements
Python 3.6+
pandas
numpy
yfinance
matplotlib
seaborn
You can install the required packages using the following command:

bash
Copy code
pip install pandas numpy yfinance matplotlib seaborn
Usage
Functions
buy_sell
This function calculates the EMAs for the given stock, generates buy/sell signals, and computes the cumulative returns of the strategy.

Parameters:

Stock (str): The ticker symbol of the stock (e.g., 'MSFT').
start (str): The start date for the historical data in 'YYYY-MM-DD' format.
end (str): The end date for the historical data in 'YYYY-MM-DD' format.
ema_1 (int): The span for the shorter EMA.
ema_2 (int): The span for the longer EMA.
capital_per_trade (float): The amount of capital allocated per trade.
Returns:

df (DataFrame): The dataframe containing historical data, EMAs, positions, daily P&L, and cumulative returns.
dt (DataFrame): The dataframe containing buy/sell signals.
Stats
This function calculates various performance metrics of the strategy.

Parameters:

data (DataFrame): The dataframe returned by the buy_sell function.
Returns:

stat (DataFrame): The dataframe containing performance metrics.
