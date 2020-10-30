# -*- coding: utf-8 -*-
"""
Pandas includes a couple useful twists, however: for unary operations like 
negation and trigonometric functions, these ufuncs will preserve index and 
column labels in the output, and for binary operations such as addition and 
multiplication, Pandas will automatically align indices when passing the 
objects to the ufunc.
"""

import pandas as pd
import numpy as np

print('Ufuncs: Index Preservation')
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))#Series object
print(ser)
print('')
df = pd.DataFrame(rng.randint(0, 10, size = (3, 4)), 
                  columns=['A', 'B', 'C', 'D']) #DataFrame Object
print(df)
print('')
# If we apply a NumPy ufunc on either of these objects, the result will be 
# another Pandas object with the indices preserved:

print('Applying exponents to the series object:')
print(np.exp(ser))
print('')
print('Applying a complex calculation on the DataFrame:')
print(np.sin(df * np.pi / 4))