# -*- coding: utf-8 -*-
"""
Pandas has built-in data aggregation methods, such as mean(), sum(), and max()
For hierarchically indexed data, these can be passed a level parameter that
controls which subset of the data the aggregate is computed on.
"""
import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], 
                            ['HR', 'Temp']], names=['subject', 'type'])

data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
health_data = pd.DataFrame(data, index=index, columns=columns)
print('Health Data:')
print(health_data)
print('Calculating the average data in the two visits each year')
data_mean = health_data.mean(level='year')
print(data_mean)
print('')
# By further making use of the axis keyword, we can take the mean among levels
# on the columns as well:
print(data_mean.mean(axis=1, level='type'))

# Thus in two lines, we’ve been able to find the average heart rate and 
# temperature measured among all subjects in all visits each year.
