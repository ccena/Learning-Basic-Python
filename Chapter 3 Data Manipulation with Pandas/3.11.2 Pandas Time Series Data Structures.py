# -*- coding: utf-8 -*-
"""
For time stamps, Pandas provides the Timestamp type.
For time periods, Pandas provides the Period type.
For time deltas or durations, Pandas provides the Timedelta type.
Timestamp and DatetimeIndex objects are invoked by using the pd.to_datetime() 
function, which can parse a wide variety of formats.
"""

import pandas as pd
import datetime

dates = pd.to_datetime([datetime.datetime(2015, 7, 3), '4th of July, 2015',
                        '2015-Jul-6', '07-07-2015', '20150708'])
print('Passing a series of dates by default yields a DatetimeIndex')
print(dates)
print('A TimedeltaIndex is created when one date is subtracted from another:')
print(dates - dates[0]); print('')


# Pandas offers a few functions to make the creation of regular date sequences 
# more convenient
print('Regular sequences: pd.date_range()')
print('Specifying a start-and endpoint:')
date_range = pd.date_range('2015-07-03', '2015-07-10')
print(date_range) #'D' denotes daily frequency

print('Specifying a startpoint and a number of periods: ')
print(pd.date_range('2015-07-03', periods=10))

print('Hourly Stamps Example: ')
x = pd.date_range('2015-07-03', periods=8, freq='H')
print(x); print('')

# pd.period_range() and pd.timedelta_range() functions create regular sequences 
# of period or time delta values
print('Monthly Periods Example:')
y= pd.period_range('2015-07', periods=8, freq='M')
print(y); print('')

print('Sequence of durations increasing by an hour:')
print(pd.timedelta_range(0, periods=10, freq='H'))