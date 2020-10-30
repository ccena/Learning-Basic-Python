# -*- coding: utf-8 -*-
"""
Instead of using groupby with so many methods for aggregation, 
the preceding operation can be simplified by using the pivot_table method
of DataFrames
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head()); print('')
print('Survivors in terms of Sex and Class:')
survivors = titanic.pivot_table('survived', index='sex', columns='class')
print(survivors); print('')

print('Multilevel pivot tables')
# The grouping in pivot tables can be specified with multiple levels,
# and via a number of options
# One can bin the age using pd.cut function
age = pd.cut(titanic['age'], [0, 18, 80])
survivors_age = titanic.pivot_table('survived', ['sex', age], 'class')
print(survivors_age); print('')

# We can apply this same strategy when working with the columns as well; let’s 
# add info on the fare paid using pd.qcut to automatically compute quantiles:
fare = pd.qcut(titanic['fare'], 2)
survivors_age_fare = titanic.pivot_table('survived',
                                         ['sex', age], 
                                         [fare, 'class'])
print('Survivors in terms of age, class, and fare')
print(survivors_age_fare)
print('The result is a four-dimensional aggregation with hierarchical indices')
print('')

print('Additional pivot table options:')
# call signature as of Pandas 0.18
# DataFrame.pivot_table(data, values=None, index=None, columns=None,
#                       aggfunc='mean', fill_value=None, margins=False,
#                       dropna=True, margins_name='All')
# The aggfunc keyword controls what type of aggregation is applied, which is a 
# mean by default.

print(titanic.pivot_table(index='sex', columns='class',
                          aggfunc={'survived':sum, 'fare':'mean'}))
print('')
# The aggfunc keyword controls what type of aggregation is applied, which is a 
# mean by default. Other several common choices are ('sum', 'mean', 'count', 
# 'min', 'max', etc.) or a function that implements an aggregation (np.sum(), 
# min(), sum(), etc.).
print('Computing totals along each grouping using margins keyword:')
print(titanic.pivot_table('survived', index='sex',
                          columns='class', margins=True))
# Here this automatically gives us information about the class-agnostic survival
# rate by gender, the gender-agnostic survival rate by class, and the overall 
# survival rate of 38%.


