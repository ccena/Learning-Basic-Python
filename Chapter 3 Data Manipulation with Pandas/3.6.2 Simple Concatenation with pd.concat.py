# -*- coding: utf-8 -*-
"""
Pandas has a function, pd.concat(), which has a similar syntax to np.concatenate
but contains a number of options.
"""
import pandas as pd

# Signature in Pandas v0.18
# pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
#           keys=None, levels=None, names=None, verify_integrity=False,
#           copy=True)
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
print('Series 1: ') ; print(ser1)
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print('Series 2: ') ; print(ser2); 
print('Combining Series 1 and 2:'); print(pd.concat([ser1, ser2]))
print('')

# It also works to concatenate higher-dimensional objects, such as DataFrames:
print('Concatenating higher-dimensional objects:')
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print('df1: '); print(df1); print('df2: '); print(df2)
print('Combining the df1 and df2:')    
print(pd.concat([df1, df2], axis = 0))
print('')
df3 = make_df('AB', [0, 1])
df4 = make_df('AB', [0, 1])
print('df3: '); print(df3); print('df4: '); print(df4)
print('Combining the df3 and df4:')    
print(pd.concat([df3, df4], axis = 1))
print('')
print('Duplicate indices')
# Pandas concatenation preserves indices, even if the result will have 
# indices!
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index # make duplicate indices!
print('x: '); print(x); print('y:'); print(y); print('Combining the x and y:') 
print(pd.concat([x, y]))
print('Now the indices are preserved, although it is undesirable.')
# Notice the repeated indices in the result. While this is valid within
# DataFrames, the outcome is often undesirable. pd.concat() gives us a few ways
# to handle it. 
print('')
print('Catching the repeats in the combination of x and y')
print('This is done by using verify_integrity=True in pd.concat:')
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)
print('')
print('Ignoring the index')
print('x: '); print(x); print('y:'); print(y); 
print('Combining the x and y while ignoring the index:')
print(pd.concat([x, y], ignore_index=True))
print('')

print('Adding MultiIndex keys')
print('x: '); print(x); print('y:'); print(y);
print(pd.concat([x, y], keys=['x', 'y']))
print('This result is a hierarchically indexed series containing the data')
print('')

print('Concatenation with joins')
print('The pd.concat has options for data with different sets of column names')
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
print('df5: '); print(df5); print('df6:'); print(df6)
print('Combining the df5 and df6:')  
print(pd.concat([df5, df6]))
print('To remove the NaN values, we use join and join_axes parameters')
# the join is a union of the input columns (join='outer'), but we can change
# this to an intersection of the columns using join='inner':
print('Combining the df5 and df6 while removing NaN columns:')  
print(pd.concat([df5, df6], join='inner'))
print('')

print('The append() method')
# Series and DataFrame objects have an append method that can accomplish the 
# same thing in fewer keystrokes
# Instead of pd.concat([df1, df2]), one can simply call df1.append(df2)

print('Combining df1 and df2 with append():')
print(df1.append(df2))

# the append() method in Pandas does not modify the original object—instead,
# it creates a new object with the combined data.






