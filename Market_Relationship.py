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
    iShares_China_ETF_df = iShares_China_ETF.history(period='6mo')
    iShares_China_ETF_df = iShares_China_ETF_df.loc[:, ['Close']]
    iShares_China_ETF_df = iShares_China_ETF_df.rename(columns={'Close':
                                                                'MCHI-CLOSE'})
    iShares_China_ETF_df = iShares_China_ETF_df.loc[iShares_China_ETF_df.index
                                                    >= '2020-01-21']

    SPY = yf.Ticker('SPY')
    SPY_df = SPY.history(period='6mo')
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
            '2020-01-30': 9821, '2020-01-31': 11948, '2020-02-01': 14551,
            '2020-02-02': 17387, '2020-02-03': 20626, '2020-02-04': 24553,
            '2020-02-05': 28276, '2020-02-06': 31439, '2020-02-07': 34876,
            '2020-02-08': 37552, '2020-02-09': 40553, '2020-02-10': 43099,
            '2020-02-11': 44919, '2020-02-12': 60326, '2020-02-13': 64438,
            '2020-02-14': 67100, '2020-02-15': 69197, '2020-02-16':71329,
            '2020-02-17': 73332, '2020-02-18': 75184, '2020-02-19': 75700,
            '2020-02-20': 76677, '2020-02-21': 77673, '2020-02-22': 78651,
            '2020-02-23': 79205, '2020-02-24': 80087, '2020-02-25': 80828,
            '2020-02-26': 81820, '2020-02-27': 83112, '2020-02-28': 84615,
            '2020-02-29': 86604, '2020-03-01': 88581, '2020-03-02': 90439,
            '2020-03-03': 93012, '2020-03-04': 95315, '2020-03-05': 98424,
            '2020-03-06': 102049, '2020-03-07': 106099, '2020-03-08': 109991,
            '2020-03-09': 114381, '2020-03-10': 118948, '2020-03-11': 126214,
            '2020-03-12': 134576, '2020-03-13': 145483, '2020-03-14':156653,
            '2020-03-15': 169593, '2020-03-16': 182490}

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

    # Add number of deaths from virus as well
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
