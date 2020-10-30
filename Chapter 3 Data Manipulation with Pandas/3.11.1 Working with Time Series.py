# -*- coding: utf-8 -*-
"""
Time stamps reference particular moments in time (e.g., July 4th, 2015, at 7:00
a.m.)
Time intervals and periods reference a length of time between a particular 
beginning and end point.
Time deltas or durations reference an exact length of time (e.g., a duration of
22.56 seconds).
"""

import pandas as pd
import numpy as np


date = pd.to_datetime("4th of July, 2015")
print('Date:', date)
print('Day of the Week:', date.strftime('%A'))
print(date + pd.to_timedelta(np.arange(12), 'D'))


print('Pandas Time Series: Indexing by Time')
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data)

