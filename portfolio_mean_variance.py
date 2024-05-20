#%%
import warnings
warnings.filterwarnings("ignore")
def action_with_warnings():
    warnings.warn("should not appear")
with warnings.catch_warnings(record=True):
    action_with_warnings()

from zipline.api          import (
    set_commission, 
    set_slippage,
    symbol, 
    symbols, 
    schedule_function, 
    order_target_percent,
)
from zipline.finance      import slippage   as slippage_lib
from zipline.finance      import commission as commission_lib
from zipline.utils.events import date_rules, time_rules
from zipline              import run_algorithm
from datetime             import datetime
import pandas             as pd
import numpy              as np
import quantstats         as qs
import matplotlib.pyplot  as plt
import riskfolio          as rp


#%%


#%%


#%%
class CustomCostModel(commission_lib.CommissionModel):
    def __init__(self, buy_cost, sell_cost):
        self.buy_cost  = buy_cost
        self.sell_cost = sell_cost
    def calculate(self, order, transaction):
        if transaction.amount > 0:
            cost = self.buy_cost
        else:
            cost = self.sell_cost
        return abs(transaction.amount)*cost


def initialize(context):
    context.assets = symbols(
        'JCI', 'TGT', 'CMCSA', 'CPB', 'MO', 'APA', 'MMC', 
        'JPM', 'ZION', 'PSA', 'BAX', 'BMY', 'LUV', 
        'PCAR', 'TXT', 'TMO', 'DE', 'MSFT', 'HPQ', 
        'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA'
    )
    context.dataset_start = None
    set_slippage(slippage_lib.FixedSlippage(spread=0.0011))
    set_commission(CustomCostModel(buy_cost=0.0036, sell_cost=0.0081))
    schedule_function(rebalance, date_rules.week_start(), time_rules.market_open())

    context.optimization_months = 24
    context.optimization_window = pd.Timedelta(days=context.optimization_months * 30)
    context.dataset_start = None


def rebalance(context, data):
    if context.dataset_start is None:
        context.dataset_start = data.current_dt

    group_start_date = data.current_dt
    if (group_start_date - context.dataset_start) < context.optimization_window:
        return

    optimization_prices_df  = data.history(context.assets, 'price', context.optimization_window.days, '1d')
    optimization_returns_df = optimization_prices_df.pct_change().dropna()

    portfolio_optimizer     = rp.Portfolio(returns=optimization_returns_df)
    portfolio_optimizer.assets_stats(method_mu='hist', method_cov='hist', d=0.94)
    optimized_w = portfolio_optimizer.rp_optimization(
        model = 'Classic',
        rm    = 'MV',
        hist  = True,
        rf    = 0.05,
        b     = None
    )
    allocated_weights = optimized_w['weights']
    for asset in context.assets:
        weight = allocated_weights[asset]
        order_target_percent(asset, weight)

    
def handle_data(context, data):
    pass


#%%


#%%
start_date = pd.Timestamp('2000-01-01')
end_date   = pd.Timestamp('2024-05-01')

results = run_algorithm(
    start          = start_date,
    end            = end_date,
    initialize     = initialize,
    handle_data    = handle_data,
    capital_base   = 10000,
    data_frequency = 'daily',
    bundle         = 'norgatedata-sp500' # 'quandl'
)

results['returns'].cumsum().plot()

#%%
results

#%%

#%%
qs.reports.basic(results['returns'])


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

