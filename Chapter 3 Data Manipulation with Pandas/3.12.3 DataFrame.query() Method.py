# -*- coding: utf-8 -*-
"""
The DataFrame has another method based on evaluated strings, called the query()
method.this is an expression involving columns of the DataFrame. It cannot be 
expressed using the DataFrame.eval() syntax, however! Instead, for this type 
of filtering operation, you can use the query() method:
"""


import pandas as pd
import numpy as np


rng = np.random.RandomState(42)
df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
print('Data:')
print(df.head())

result1 = df[(df.A < 0.5) & (df.B < 0.5)]
result2 = pd.eval('df[(df.A < 0.5) & (df.B < 0.5)]')
print('Data after eval():')
print(result2.head())
print(np.allclose(result1, result2))

# query() allows selection using an expression
result2 = df.query('A < 0.5 and B < 0.5')
np.allclose(result1, result2)

# query() method also accepts the @ flag to mark local variables
Cmean = df['C'].mean()
result1 = df[(df.A < Cmean) & (df.B < Cmean)]
result2 = df.query('A < @Cmean and B < @Cmean')
print(result2.head())
print(np.allclose(result1, result2))