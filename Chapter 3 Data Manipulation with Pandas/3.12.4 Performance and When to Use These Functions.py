# -*- coding: utf-8 -*-
"""
When considering whether to use these functions eval() and query(), 
there are two considerations: computation time and memory use. Memory use is 
the most predictable aspect. As already mentioned, every compound expression 
involving NumPy arrays or Pandas DataFrames will result in implicit creation
of temporary arrays:

"""

import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
print('Data:')
print(df.head())
x = df[(df.A < 0.5) & (df.B < 0.5)]
print('Applying operations in the data:'); print(x.head())
tmp1 = df.A < 0.5
tmp2 = df.B < 0.5
tmp3 = tmp1 & tmp2
y = df[tmp3]
print('Equivalent data:'); print(y.head())
print(df.values.nbytes)

# eval() can be faster even when you are not maxing out your system memory.
# The benefit of eval/query is mainly in the saved memory, and the sometimes
# cleaner syntax they offer.