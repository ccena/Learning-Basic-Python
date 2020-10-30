# -*- coding: utf-8 -*-
"""
Most of Pandas’ string syntax is intuitive enough that it’s probably 
sufficient to just list a table of available methods
"""

import pandas as pd

monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
'Eric Idle', 'Terry Jones', 'Michael Palin'])
#prints the data
print('Monte:'); print(monte); print('')

print('Methods similar to Python string methods')
#returns a series of strings
print('Lower format of the data:'); print(monte.str.lower()); print('')
#returns numbers
print('Length of the data:'); print(monte.str.len()); print('')
#returns Boolean values
print(monte.str.startswith('T')); print('')
#returns lists or other compound values for each element
print(monte.str.split()); print('')

print('Methods using regular expressions')
#extract on each element returns the first name
print(monte.str.extract('([A-Za-z]+)')); print('')
#findall locates all names that start and end with a consonant 
print(monte.str.findall(r'^[^AEIOU].*[^aeiou]$')); print('')
# The ability to concisely apply regular expressions across Series or DataFrame 
# entries opens up many possibilities for analysis and cleaning of data.

print('Vectorized Slicing')
# The get() and slice() operations, in particular, enable vectorized element
# access from each array.
print(monte.str[0:3])
print(monte.str.split().str.get(1)); print('')

print('Indicator variables')
full_monte = pd.DataFrame({'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C',
                                    'B|C|D'], 'name': monte})
print(full_monte)
# The get_dummies() routine lets you quickly split out these indicator 
# variables into a DataFrame:
print(full_monte['info'].str.get_dummies('|'))

