# -*- coding: utf-8 -*-
"""
It is possible to define even more advanced compound types. For example, 
you can create a type where each element contains an array or matrix of values.
"""

import numpy as np

# Here, we’ll create a data type with a mat component consisting of a 
# 3×3 floating-point matrix:
    
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])

# Now each element in the X array consists of an id and a 3×3 matrix.
# If you find yourself writing a Python interface to a legacy C or Fortran 
# library that manipulates structured data, you’ll probably find structured
# arrays quite useful!