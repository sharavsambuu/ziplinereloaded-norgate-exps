@echo off

zipline run -f helloworld.py -b norgatedata-aapl --start 2014-1-1 --end 2020-1-1 -o helloworld.pickle --no-benchmark
