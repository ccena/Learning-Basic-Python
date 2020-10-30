# -*- coding: utf-8 -*-
"""
A pivot table is a similar operation that is commonly seen in spreadsheets and
other programs that operate on tabular data. The pivot table takes simple 
columnwise data as input, and groups the entries into a two-dimensional table
that provides a multidimensional summarization of the data.
"""


import seaborn as sns

print('Pivot tables are essentially a multidimensional version of GroupBy aggregation.')
print('Motivating Pivot Tables')

titanic = sns.load_dataset('titanic')
print(titanic.head()); print('')
# This contains a wealth of information on each passenger of that ill-fated 
# voyage, including gender, age, class, fare paid, and much more.

print('Pivot Tables by Hand')
print(titanic.groupby('sex')[['survived']].mean()); print('')
#This result gives some insight of the number of males and females that have
# survived. 

# Using the vocabulary of GroupBy, we might proceed using something
# like this: we group by class and gender, select survival, apply a mean 
# aggregate, combine the resulting groups, and then unstack the hierarchical 
# index to reveal the hidden multidimensionality
print(titanic.groupby(['sex', 'class'])['survived'].mean().unstack())
