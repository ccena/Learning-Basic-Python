# -*- coding: utf-8 -*-
"""
DataFrame acts in many ways like a two-dimensional or structured array, and 
in other ways like a dictionary of Series structures sharing the same index.
"""

import pandas as pd

print('DataFrame as a dictionary')
area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
print('Data:')
print(data)

# The individual Series that make up the columns of the DataFrame can be
# accessed via dictionary-style indexing of the column name:
print('')
print("Accessing Area via Dictionary Style Indexing, data['area']: ")
print(data['area'])
print('')
print("Accessing Area via Attribute Style Indexing, data.area: ")
print(data.area)
print('')
print('Are both styles of accessing the DataFrame equal?')
print(data.area is data['area'])
print('')
print('Modifying the data by adding a Density column:')
data['density'] = data['pop'] / data['area']
print(data)
print('')
print('DataFrame as two-dimensional array')
print(data.values)
print('')
print('Transposing the full DataFrame to swap rows and columns:')
print(data.T)
print('')

# In a DataFrame, passing a single index to an array accesses a row
print('Accessing the first row via data.values[0]:', data.values[0])
# Passing a single “index” to a DataFrame accesses a column
print('')
print("Acessing the area column via data['area']:")
print(data['area'])
print('')
# For better array style indexing, one can use loc, iloc, and ix indexers
# Note: The DataFrame index and column labels are maintained in the result
print("Acessing the area and population column via data.iloc[]:")
print(data.iloc[:5, :2])
print('')
print("Acessing the area and population column via data.loc[]:")
print(data.loc[:'Illinois', :'pop'])
print('')
print('Combining the loc indexer with masking and fancy indexing:')
print(data.loc[data.density > 100, ['density', 'pop', 'area']])
print('')
print('Combining the iloc indexer to modify values: ')
data.iloc[0, 2] = 90
print(data)
print('')

print('Additional indexing conventions')
# In DataFrames while indexing refers to columns, slicing refers to rows:
print('Slicing from New York to Illinois:')
print(data['New York':'Illinois'])
print('')
print('Slicing data using index: ')
print(data[2:5])
print('')
#direct masking operations are also interpreted row-wise rather than
#column-wise:
print('Masking a row:')
print(data[data.density > 100])
    
