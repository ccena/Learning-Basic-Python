# -*- coding: utf-8 -*-
"""
Simple aggregations can give you a flavor of your dataset, but often we would
prefer to aggregate conditionally on some label or index. This can be done 
with the so-called groupby operation.
"""
import seaborn as sns
import pandas as pd
import numpy as np

print('PLANETS DATA')
planets = sns.load_dataset('planets')
print(planets.shape)
print(planets.head()); print('')


print('Split, apply, combine')
# •The split step involves breaking up and grouping a DataFrame depending on 
# the value of the specified key.
# • The apply step involves computing some function, usually an aggregate,
# transformation, or filtering, within the individual groups.
# • The combine step merges the results of these operations into an output 
# array.

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
print('Data Frame:'); print(df)
# Creating a DataFrameGroupBy object
print(df.groupby('key'))
print('Sum:'); print(df.groupby('key').sum()); print('')
# the most important operations made available by a GroupBy are aggregate,
# filter, transform, and apply.

print('Column indexing using Groupby')
# The GroupBy object supports column indexing in the same way as
# the DataFrame, and returns a modified GroupBy object.
print(planets.groupby('method'))
print(planets.groupby('method')['orbital_period'])
# Here we’ve selected a particular Series group from the original DataFrame 
# group by reference to its column name.
print('The general scale of orbital periods (in days) in each method:')
print(planets.groupby('method')['orbital_period'].median()); print('')

# The GroupBy object supports direct iteration over the groups,
# returning each group as a Series or DataFrame
print('Iteration over groups:')
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape)); 
print('')
# This can be useful for doing certain things manually, though it is often
# much faster to use the built-in apply functionality, which we will discuss
# momentarily.

print('Dispatch methods')
# you can use the describe() method of DataFrames to perform a set of 
# aggregations that describe each group in the data:
disp = planets.groupby('method')['year'].describe()
print(disp); print('')

message = 'Groupby: Aggregate, filter, transform, and apply'
print(message.upper())
# In particular, GroupBy objects have aggregate(),filter(), transform(), and 
# apply() methods that efficiently implement a variety of useful operations 
# before combining the grouped data.
rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns = ['key', 'data1', 'data2'])

print('Data:')
print(df); print('')
print('Aggregation:')
aggre1 = df.groupby('key').aggregate(['min', np.median, max])
print(aggre1); print('')
# Another useful pattern is to pass a dictionary mapping column names to 
# operations to be applied on that column:
aggre2 = df.groupby('key').aggregate({'data1': 'min',
                             'data2': 'max'})
print('Mapping column names with a dictionary:')
print(aggre2); print('')

print('Filtering Data:')
# A filtering operation allows you to drop data based on the group properties
def filter_func(x):
    return x['data2'].std() > 4 #keeping all groups with standard dev > 4 
print(df); print(df.groupby('key').std());
print(df.groupby('key').filter(filter_func)); print('')

print('Transformation')
# transformation can return some transformed version of the full data to 
# recombine. For such a transformation, the output is the same shape as
# the input.
transf = df.groupby('key').transform(lambda x: x - x.mean())
print(transf)

print('The apply() method')
# The apply() method lets you apply an arbitrary function to the
# group results. The function should take a DataFrame, and return either 
# a Pandas object (e.g., DataFrame, Series) or a scalar

def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x
print('df:'); print(df); 
print('Normalized data1 of df:'); print(df.groupby('key').apply(norm_by_data2))


