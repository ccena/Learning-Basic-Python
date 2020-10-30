# -*- coding: utf-8 -*-
"""
The data is about bicycle counts on Seattle’s Fremont Bridge. 
This data comes from an automated bicycle counter, installed in late 2012, 
which has inductive sensors on the east and west sidewalks of the bridge.
http://data.seattle.gov/
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import numpy as np

data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
print(data.head()) #accessing the first 5 values
data.columns = ['Total', 'East', 'West'] #formatting the column labels
aggre_data = data.dropna().describe() #data statistic summary
print(aggre_data)

#visualizing the data
data.plot() #plotting the data
plt.ylabel('Hourly Bicycle Count');

#The data is too dense and needs to be resampled
weekly = data.resample('W').sum() #creating weekly samples
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count');

#creating daily samples
daily = data.resample('D').sum()
#aggregating the data using pd.rolling_mean()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-']) #30-day roll
plt.ylabel('mean hourly count');

#smoothening the jagged curve using a window function 
daily.rolling(50, center=True,
              win_type='gaussian').sum(std=10).plot(style=[':', '--', '-']);

#digging into the data
by_time = data.groupby(data.index.time).mean()#taking the hourly mean
#average traffic as a function of the time of day
hourly_ticks = 4 * 60 * 60 * np.arange(6)#creating a 24-hour format
#hourly traffic is bimodal peaking at 8am and 5pm
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-']);

#looking at bicycle counts based on the day of the week
by_weekday = data.groupby(data.index.dayofweek).mean()#taking the weekly mean
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-']);

#looking at the hourly trend on weekdays versus weekends
#creating a new column of weedays and weekends
weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_time.loc['Weekday'].plot(ax=ax[0], title='Weekdays',
                           xticks=hourly_ticks, style=[':', '--', '-'])
by_time.loc['Weekend'].plot(ax=ax[1], title='Weekends',
                           xticks=hourly_ticks, style=[':', '--', '-']);
    
