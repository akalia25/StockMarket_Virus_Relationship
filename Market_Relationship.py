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
    iShares_China_ETF_DF = iShares_China_ETF_DF.loc[:,['Close']]
    iShares_China_ETF_DF = iShares_China_ETF_DF.rename(columns={'Close':'MCHI-CLOSE'})

    SPY = yf.Ticker('SPY')
    SPY_DF = SPY.history(period='1mo')
    SPY_DF.loc[:,'StockName'] = 'SPY'
    SPY_DF = SPY_DF[['Close']]
    SPY_DF = SPY_DF.rename(columns={'Close':'SPY-CLOSE'})
    frames = [SPY_DF, iShares_China_ETF_DF]
    stock_market_df = pd.concat(frames, axis=1)

    normalized_market = stock_market_df.iloc[0]/stock_market_df