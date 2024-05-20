#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Norgate data bundle ingestion description

from norgatedata import StockPriceAdjustmentType
from zipline_norgatedata import (
        register_norgatedata_equities_bundle,
        register_norgatedata_futures_bundle
        )

from pathlib import Path
from zipline.data.bundles import register
from zipline.data.bundles.ingester import csv_ingester # ingester.py need to be placed in zipline.data.bundles

_DEFAULT_PATH = str(Path.home() / '.zipline/csv/yahoo')

register(
    'yahoo_csv',
    csv_ingester('YAHOO',
                 every_min_bar=False, # the price is daily
                 csvdir_env='YAHOO_CSVDIR',
                 csvdir=_DEFAULT_PATH,
                 index_column='Date',
                 column_mapper={'Open': 'open',
                                'High': 'high',
                                'Low': 'low',
                                'Close': 'close',
                                'Volume': 'volume',
                                'Adj Close': 'price',
                 },
    ),
    calendar_name='NYSE',
)

from zipline.data.bundles.ingester import direct_ingester

from zipline.data.bundles import yahoo
register('yahoo_direct', # bundle's name
         direct_ingester('YAHOO',
                         every_min_bar=False,
                         symbol_list_env='YAHOO_SYM_LST', # the environemnt variable holding the comma separated list of assert names
                         downloader=yahoo.get_downloader(start_date='2010-01-01',
                                                         end_date='2024-10-01'
                         ),
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import iex
import exchange_calendars as xcals

cal=xcals.get_calendar('NYSE')
register('iex', # bundle's name
         direct_ingester('IEX Cloud',
                         every_min_bar=False,
                         symbol_list_env='IEX_SYM_LST', # the environemnt variable holding the comma separated list of assert names
                         downloader=iex.get_downloader(start_date='2020-01-01',
                                                       end_date='2024-10-01'
                         ),
                         filter_cb=lambda df: df[[cal.is_session(dt) for dt in df.index]]
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import binance

register('binance_daily', # bundle's name
         direct_ingester('Binance Exchange',
                         every_min_bar=False,
                         symbol_list_env='BINANCE_SYM_LST', # the environemnt variable holding the comma separated list of assert names
                         downloader=binance.get_downloader(start_date='2020-01-01',
                                                           end_date='2024-10-01',
                                                           every_min_bar=False # True for minute price, False for dailyprice
                         ),
         ),
         calendar_name='24/7',
)

register('binance_min', # bundle's name
         direct_ingester('Binance Exchange',
                         every_min_bar=True,
                         symbol_list_env='BINANCE_SYM_LST', # the environemnt variable holding the comma separated list of assert names
                         downloader=binance.get_downloader(start_date='2020-01-01',
                                                           end_date='2024-10-01',
                                                           every_min_bar=True # True for minute price, False for dailyprice
                         ),
         ),
         calendar_name='24/7',
)





# EQUITIES BUNDLES

# Single stock bundle - AAPL from 1990 though 2018
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-aapl',
    symbol_list = ['AAPL','$SPXTR',], 
    start_session = '1990-01-01',
    end_session = '2020-12-01'
)

# FANG stocks (Facebook, Amazon, Netflix, Google) - 2012-05-18 until now
# (is now really MANG !)
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-fang',
    symbol_list = ['META','AMZN','NFLX','GOOGL','$SPXTR',], 
    start_session = '2012-05-18',  # This is that FB (now META) first traded
)

# A small set of selected ETFs
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-selected-etfs',
    symbol_list = ['SPY','GLD','USO','$SPXTR',],
    start_session = '2006-04-10', # This is the USO first trading date
)

# S&P 500 Bundle for backtesting including all current & past constituents back to 1990
# and the S&P 500 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 1800 securities)
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp500',
    symbol_list = ['$SPXTR'],
    watchlists = ['S&P 500 Current & Past'],
    start_session = '1970-01-01',
)

# Russell 3000 bundle containing all ccurrent & past constituents back to 1990
# and the Russell 3000 Total Return Index (useful for benchmarking and/or index trend filtering)
# (about 11000 securities)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-russell3000',
    watchlists = ['Russell 3000 Current & Past'],
    symbol_list = ['$RUATR'],
    start_session = '1990-01-01' ,
)

# And now a watchlist excluding a given list of symbols

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-russell3000-exfroth',
    watchlists = ['Russell 3000 Current & Past'],
    symbol_list = ['$RUATR'],
    start_session = '1990-01-01' ,
    excluded_symbol_list = ['TSLA','AMZN','META','NFLX','GOOGL',]
)

# FUTURES BUNDLES

# Example bundle for all of the individual contracts from three futures markets:
# E-mini S&P 500, E-mini Nasdaq 100, E-mini Russell 2000,
# with $SPXTR added for benchmark reference
#register_norgatedata_futures_bundle(
#    bundlename = 'norgatedata-selected-index-futures',
#    session_symbols = ['ES','NQ','RTY'],
#    symbol_list = ['$SPXTR'],
#    start_session = '2000-01-01',
#)
