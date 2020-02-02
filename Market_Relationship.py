#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:10:46 2020

@author: adityakalia
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

def stock_market_data():
    iShares_China_ETF = yf.Ticker('MCHI')
    iShares_China_ETF_df = iShares_China_ETF.history(period='1mo')
    iShares_China_ETF_df = iShares_China_ETF_df.loc[:, ['Close']]
    iShares_China_ETF_df = iShares_China_ETF_df.rename(columns={'Close':
                                                                'MCHI-CLOSE'})
    iShares_China_ETF_df = iShares_China_ETF_df.loc[iShares_China_ETF_df.index
                                                    >= '2020-01-21']

    SPY = yf.Ticker('SPY')
    SPY_df = SPY.history(period='1mo')
    SPY_df.loc[:, 'StockName'] = 'SPY'
    SPY_df = SPY_df[['Close']]
    SPY_df = SPY_df.rename(columns={'Close': 'SPY-CLOSE'})
    SPY_df = SPY_df.loc[SPY_df.index >= '2020-01-21']
    frames = [SPY_df, iShares_China_ETF_df]
    stock_market_df = pd.concat(frames, axis=1)

    normalized_market = stock_market_df/stock_market_df.iloc[0]

    return normalized_market

def virus_data():
    # Data Obtained from https://www.worldometers.info/coronavirus/
    virus_data = {'2020-01-21': 446, '2020-01-22': 579, '2020-01-23': 844,
            '2020-01-24': 1312, '2020-01-25': 2015, '2020-01-26': 2801,
            '2020-01-27': 4579, '2020-01-28': 6061, '2020-01-29': 7816,
            '2020-01-30': 9821, '2020-01-31': 11948, '2020-02-01': 14551}

    date_index = virus_data.keys()
    date_index = [datetime.strptime(x, '%Y-%m-%d') for x in date_index]
    virus_df = pd.DataFrame(virus_data.values(), index=date_index,
                            columns=['number_of_cases'])
    virus_df.index.name = 'Date'
    virus_df_norm = virus_df/virus_df.iloc[0]

    return virus_df

def market_virus_plot():
    market_df = stock_market_data()
    virus_df = virus_data()
    time = market_df.index
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Normalized_Market_Values', color=color)
    ax1.plot(market_df.index, market_df.iloc[:,0], color=color, label='SPY-CLOSE')
    ax1.plot(market_df.index, market_df.iloc[:,1], color='orange', label='MCHI-CLOSE')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend()


    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Number of Cases', color=color)  # we already handled the x-label with ax1
    ax2.plot(virus_df.index, virus_df, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.autofmt_xdate()
    plt.savefig('Screenshots/Market_Virus_Relationship.png', dpi=72,
                    bbox_inches='tight')
    plt.show()


def main():
    market_df = stock_market_data()
    virus_df = virus_data()
    finaldf = pd.concat([market_df, virus_df], axis=1)
    market_df.plot()
    virus_df.plot()
    market_virus_plot()


if __name__ == '__main__':
    main()
