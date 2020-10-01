#Author:Ken Bacchiani
#Python Stocks Program

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'ZOQFPG1T7XNIEG4S'

ts = TimeSeries(key=api_key, output_format = 'pandas')
run = True
while run :
    try:
        stock = input("Enter the name of your stock. Type quit or q to end.  ")
        if stock.lower() == "quit" or stock.lower() == "q" :
            break
        if stock.isalpha() == False:
            print("Stock names only contain letters, please re enter your stock")
            continue
        intvl = input("Enter the interval for which you want to see the prices. Supported minute intervals are 1, 5, 15, 30, or 60. Daily, Weekly and monthly prices also supported. ")
        if intvl.lower() == "daily" :
            data = ts.get_daily(symbol= stock)
            print("%s Daily Stock Prices" % stock.upper())
            print(data)
        elif intvl.lower() == "weekly" :
            data = ts.get_weekly(symbol= stock)
            print("%s Weekly Stock Prices" % stock.upper())
            print(data)
        elif intvl.lower() == "monthly" :
            data = ts.get_monthly(symbol=stock)
            print("%s Monthly Stock Prices" % stock.upper())
            print(data)
        else :
            data = ts.get_intraday(symbol=stock, interval = intvl + "min", outputsize='full')
            if int(intvl) == 1 :
                print("%s Intraday Stock Prices for every %s Minute" % (stock.upper(), intvl))
            else :
                print("%s Intraday Stock Prices for every %s Minutes" % (stock.upper(), intvl))
            print(data)
    except:
        print("Invalid value entered. Try Again")
