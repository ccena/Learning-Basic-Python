# -*- coding: utf-8 -*-
"""
An essential piece of analysis of large data is efficient summarization: 
computing aggregations like sum(), mean(), median(), min(), and max(), 
in which a single number gives insight into the nature of a potentially 
large dataset. 
"""

import seaborn as sns
import pandas as pd
import numpy as np

print('PLANETS DATA')
planets = sns.load_dataset('planets')
print(planets.shape)
print(planets.head()); print('')


print('SIMPLE AGGREGATION IN PANDAS')
# For a DataFrame, by default the aggregates return results within each column:
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))    
df = pd.DataFrame({'A': rng.rand(5),'B': rng.rand(5)})
print('Mean for each column:')
print(df.mean()); print('')

# By specifying the axis argument, you can instead aggregate within each row:
print('Mean of each row:')
print(df.mean(axis='columns')); print('')


# there is a convenience method describe() that computes several common 
# aggregates for each column and returns the result.
aggre_planet = planets.dropna().describe()
print(aggre_planet)
# This can be a useful way to begin understanding the overall properties of a 
# dataset