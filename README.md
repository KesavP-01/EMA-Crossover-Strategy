
# Technical Strategy Analysis

## Overview
This project implements a simple trading strategy based on the Exponential Moving Average (EMA) crossover. The script downloads historical stock data, calculates EMAs, generates buy/sell signals, and evaluates the performance of the strategy with various metrics.



## Parameters:

- **Stock (str)**: The ticker symbol of the stock (e.g., 'MSFT').
- **start (str)**: The start date for the historical data in 'YYYY-MM-DD' format.
- **end (str)**: The end date for the historical data in 'YYYY-MM-DD' format.
- **ema_1 (int)**: The span for the shorter EMA.
- **ema_2 (int)**: The span for the longer EMA.
- **capital_per_trade (float)**: The amount of capital allocated per trade.

## Returns:
- **df (DataFrame)**: The dataframe containing historical data, EMAs, positions, daily P&L, and cumulative returns.
- **dt (DataFrame)**: The dataframe containing buy/sell signals.


## Results

![MSFT Year Signals](https://github.com/KesavP-01/EMA-Crossover-Strategy/assets/161378031/478a7385-1b2d-47e9-a989-5fca5b4abe87)

#### Achieved a Cummulative return of 26.33% over 3 years for MSFT stock, while placing 5 trades
