# -*- coding: utf-8 -*-
"""
Data provided by Centers for Disease Control
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np

#reading the data
births = pd.read_csv('births.csv')
print('Head of the data:') 
print(births.head()) #prints the first five data values
print('')
#adding a decade column into the data
births['decade'] = 10 * (births['year'] // 10) # Calculate the decade
print(births.pivot_table('births', index='decade', 
                         columns='gender', aggfunc='sum'))
message = 'We immediately see that male births outnumber female births'
message += ' in every decade.'
print(message)

sns.set() #use Seaborn styles
birth_gender = births.pivot_table('births', index='year',
                                  columns='gender', aggfunc='sum')
birth_gender.plot() #generate a gender plot from the data
plt.ylabel('total births per year'); print('')
#over the past 50 years male births outnumbered female births by around 5%.

print('Further Data Exploration:')
quartiles = np.percentile(births['births'], [25, 50, 75]) #
mu = quartiles[1]
#remove mistyped dates & missing values via sigma-clipping operation
sig = 0.74 * (quartiles[2] - quartiles[0]) 

#use query() to filter out rows w/ births outside the sigma values.
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
#set 'day' column to integer; it originally was a string due to nulls
births['day'] = births['day'].astype(int)

#create a datetime index from the year, month, day
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek
births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');
print('Births are slightly less common on weekends than on weekdays!')
print('')

births_by_date = births.pivot_table('births', [births.index.month, 
                                               births.index.day])
print(births_by_date.head())
births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]
print(births_by_date.head())
#plot the results to obtain a time-series
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);


