import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def buy_sell(Stock, start, end, ema_1, ema_2, capital_per_trade):
    
    df = yf.download(Stock, start, end, interval='1d')
    df = df[['Adj Close']]
    df['ema_' + str(ema_1)] = df['Adj Close'].ewm(span= ema_1, min_periods=ema_1).mean()
    df['ema_' + str(ema_2)] = df['Adj Close']. ewm(span= ema_2, min_periods= ema_2).mean()
    df['position'] = 0
    df['pct_chg'] = df['Adj Close'].pct_change()
    buy = []
    sell = []
    signal = []
    
    for i in range(ema_2-1, len(df)-1):
         
        if df['position'][i] == 0:
            if df['ema_' + str(ema_1)][i] > df['ema_' + str(ema_2)][i]:
                df['position'][i+1] = 1
                buy.append(df['Adj Close'][i+1])
                sell.append(np.nan)
                signal.append(1)
                
            elif df['ema_' + str(ema_1)][i] < df['ema_' + str(ema_2)][i]:
                df['position'][i+1] = -1
                buy.append(np.nan)
                sell.append(df['Adj Close'][i+1])
                signal.append(0)
                
        elif df['position'][i] ==1:
            if df['ema_' + str(ema_1)][i] < df['ema_' + str(ema_2)][i]:
                df['position'][i+1] = 0
                buy.append(np.nan)
                sell.append(np.nan)
                signal.append(np.nan)
            
            else:
                df['position'][i+1] =1
                buy.append(np.nan)
                sell.append(np.nan)
                signal.append(np.nan)
            
        elif df['position'][i] == -1:
            if df['ema_' + str(ema_1)][i] > df['ema_' + str(ema_2)][i]:
                df['position'][i+1] = 0
                buy.append(np.nan)
                sell.append(np.nan)
                signal.append(np.nan)

                
            else:
                df['position'][i+1] = -1
                buy.append(np.nan)
                sell.append(np.nan)
                signal.append(np.nan)
    
                
    df['daily_pnl'] = df['position'] * df['pct_chg']
    df['cum_ret'] = (1+df['daily_pnl'] * capital_per_trade).cumprod() -1
    df.dropna(inplace=True)
    dt = pd.DataFrame({'Buy_price': buy,
                       'Sell_price': sell,
                       'Signal': signal})
    dt.loc[-1] = [np.nan, np.nan, np.nan]
    dt.index = dt.index +1
    dt.sort_index(inplace=True)
    return df, dt

def Stats(data):
    dt = data.copy()
    trades = data['position'].diff().fillna(0).astype(bool).sum(axis=0)
    
    c_return = round(data['cum_ret'][-1],4) * 100
    dt['retn'] = data['Adj Close'].pct_change()
    dt['c_ret'] = (1+dt['retn']).cumprod()
    n = len(data) / 252
    vol = dt['retn'].std() * np.sqrt(252) * 100
    
    dt['c_roll_max'] = dt['c_ret'].cummax()
    dt['drawdown'] = dt['c_roll_max'] - dt['c_ret']
    
    max_dd = (dt['drawdown'] / dt['c_roll_max']).max() * 100
    
    cagr = (dt["c_ret"][-1]**(1/n)-1) * 100
    stat = pd.DataFrame({'No_of_trades' : trades,
                         'Cummulative_return': c_return,
                         'CAGR': cagr,
                         'Max_drawdown': max_dd,
                         'Annualized_volatility': vol}, index=['0'])
    return stat
    
    
            
            
data, signals = buy_sell('MSFT', '2021-01-01', '2024-03-01', 20, 100, 0.5)
stats = Stats(data)


plt.figure(figsize=(12, 8), dpi = 400)
data['Adj Close'].plot()
data['ema_20'].plot()
data['ema_100'].plot()
plt.scatter(x= data.index, y= signals['Buy_price'], marker = '^', color= 'green', s= 200)
plt.scatter(x= data.index, y= signals['Sell_price'], marker = 'v', color= 'red', s= 200)
plt.legend(loc= 'upper left')

