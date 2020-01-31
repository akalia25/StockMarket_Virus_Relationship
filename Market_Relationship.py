#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:10:46 2020

@author: adityakalia
"""

import pandas as pd
import yfinance as yf


def stock_market_data:
    iShares_China_ETF = yf.Ticker('MCHI')
    iShares_China_ETF_DF = iShares_China_ETF.history(period='1mo')
    iShares_China_ETF_DF = iShares_China_ETF_DF.loc[:, ['Close']]
    iShares_China_ETF_DF = iShares_China_ETF_DF.rename(columns={'Close':
                                                                'MCHI-CLOSE'})

    SPY = yf.Ticker('SPY')
    SPY_DF = SPY.history(period='1mo')
    SPY_DF.loc[:, 'StockName'] = 'SPY'
    SPY_DF = SPY_DF[['Close']]
    SPY_DF = SPY_DF.rename(columns={'Close': 'SPY-CLOSE'})
    frames = [SPY_DF, iShares_China_ETF_DF]
    stock_market_df = pd.concat(frames, axis=1)

    normalized_market = stock_market_df/stock_market_df.iloc[0]

    return normalized_market

def virus_data:
    # Data Obtained from https://www.worldometers.info/coronavirus/
    virus_data = {'2020-01-21': 446, '2020-01-22': 579, '2020-01-23': 844,
            '2020-01-24': 1312, '2020-01-25': 2015, '2020-01-26': 2801,
            '2020-01-27': 4579, '2020-01-28': 6061, '2020-01-29': 7816,
            '2020-01-30': 9821}

    virus_DF = pd.DataFrame(virus_data.values(), index=virus_data.keys(),
                            columns=['number_of_cases'])

