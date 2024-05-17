#%%
#zipline --start=2011-1-1 --end=2013-1-1 --no-benchmark

from   zipline.api       import order, record, symbol, set_benchmark
from   zipline           import run_algorithm
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt


#%%
def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), "price"))
    
def analyze(context, perf):
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax2 = plt.subplot(212, sharex=ax1)
    perf.AAPL.plot(ax=ax2)
    plt.gcf().set_size_inches(18, 8)
    plt.show()

#%%


#%%
start_date   = pd.Timestamp('2011-1-1')
end_date     = pd.Timestamp('2013-1-1')
capital_base = 10000

result = run_algorithm(
    start          = start_date,
    end            = end_date,
    initialize     = initialize,
    handle_data    = handle_data,
    analyze        = analyze,
    capital_base   = capital_base,
    data_frequency = 'daily',
    bundle         = 'norgatedata-sp500'
)


#%%
list(result.keys())

#%%
result['returns'].cumsum().plot()


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

