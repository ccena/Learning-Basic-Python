# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:50:21 2020

@author: HOTs
"""
import pandas as pd

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
'food': ['fish', 'beans', 'bread']},
columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
'drink': ['wine', 'beer']},
columns=['name', 'drink'])
print('df6: '); print(df6);print('df7'); print(df7);
print('Creating df8 by combining df6 and df7:')
df8 = pd.merge(df6, df7)
print(df8)
print('The output only contains the intersections of the two sets of inputs!')
print('This is called the inner join.')
print('To change the output to return the union of the two sets, we set how = outer')
print(pd.merge(df6, df7, how='outer'))
print('')

# The left join and right join return join over the left entries and right
# entries, respectively. For example:
print('Fixing the output rows to correspond to the entries in the left input:')
print('df6: '); print(df6);print('df7'); print(df7);
print('Output:')
print(pd.merge(df6, df7, how='left'))