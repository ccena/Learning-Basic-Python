# -*- coding: utf-8 -*-
"""
The ability to use dates and times as indices to intuitively organize and
access data is an important piece of the Pandas time series tools.
"""

import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
# import datetime

goog = data.DataReader('F', start='2004', end='2016',data_source='yahoo')
print(goog.head())
goog = goog['Close']
goog.plot();
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--')
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left');

#The primary difference between the two is that resample() is fundamentally
# a data aggregation, while asfreq() is fundamentally a data selection.

print('Up-sampling the data')
fig, ax = plt.subplots(2, sharex=True)
data = goog.iloc[:10]
data.asfreq('D').plot(ax=ax[0], marker='o')
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"]); print('')

print('Time-shifts')
# Another common time series–specific operation is shifting of data in time.
# This uses shift() that shifts the data and tshift() that shifts the index
fig, ax = plt.subplots(3, sharey=True,)
# apply a frequency to the data
goog = goog.asfreq('D', method='pad')
goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])
# legends and annotations
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')
ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')
ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')
ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');
plt.figure()

ROI = 100 * (goog.tshift(-365) / goog - 1)
ROI.plot()
plt.ylabel('% Return on Investment')

print('Rolling windows')
# rolling() attribute makes available a number of aggregation operations
# by default
rolling = goog.rolling(365, center=True)
data = pd.DataFrame({'input': goog,
                     'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_std': rolling.std()})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(0.3)  