# -*- coding: utf-8 -*-
"""
The behavior of pd.merge() is a subset of what is known as relational
algebra, which is a formal set of rules for manipulating relational data, 
and forms the conceptual foundation of operations available in most databases.
"""

import pandas as pd

message = 'Categories of Joins'
print(message.upper())
print('One-to-One joins')
# Perhaps the simplest type of merge expression is the one-to-one join, 
# which is in many ways very similar to the column-wise concatenation seen

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})
print('df1:'); print(df1); print('df2:'); print(df2)
print('To combine this information into a single DataFrame, we can use the pd.merge() function')
df3 = pd.merge(df1, df2)
print('Creating df3 by combining df1 and df2:')
print(df3)
print('')
# The pd.merge() function recognizes that each DataFrame has an “employee” 
# column, and automatically joins using this column as a key.


# Many-to-one joins are joins in which one of the two key columns contains
# duplicate entries.
print('Many-to-one joins')
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
'supervisor': ['Carly', 'Guido', 'Steve']})
print('df3:'); print(df3); print('df4: '); print(df4);
print('Creating df5 by comining df4 and df3:')
df5 = pd.merge(df3, df4)
print(df5)
print('')


# If the key column in both the left and right array contains duplicates, then
# the result is a many-to-many merge. 
print('Many-to-many joins')
df6 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Engineering', 
                              'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding',
                               'linux','spreadsheets', 'organization']})

print('df1:'); print(df1); print('df6:'); print(df6)
df7 = pd.merge(df1, df6)
print('Creating df7 by comining df1 and df5:')
print(df7)          
                    




