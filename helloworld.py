from zipline.api import order_target, record, symbol

def initialize(context):
    context.i = 0 
    context.asset = symbol("AAPL")


def  handle_data(context, data):
    context.i += 1
    if context.i<300:
        return

    short_mavg = data.history(context.asset, 'price', bar_count=100, frequency='1d').mean()
    long_mavg  = data.history(context.asset, 'price', bar_count=300, frequency='1d').mean()

    if short_mavg > long_mavg:
        order_target(context.asset, 100)
    elif short_mavg<long_mavg:
        order_target(context.asset, 0)

    record(
        AAPL=data.current(context.asset, 'price'),
        short_mavg = short_mavg,
        long_mavg  = long_mavg
        )
