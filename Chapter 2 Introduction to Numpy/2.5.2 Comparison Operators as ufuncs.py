# -*- coding: utf-8 -*-
"""
NumPy also implements comparison operators such as < (less than) and > (greater 
than) as element-wise ufuncs. The result of these comparison operators is 
always an array with a Boolean data type.
"""
import numpy as np
print('Standard Comparison Operations')
x = np.array([1, 2, 3, 4, 5])
print('Values that are less than 3:', x < 3)
print('Values that are greater than 3:', x > 3)
print('Values that are less than or equal to 3:', x <= 3)
print('Values that are greater than or equal to 3:', x >= 3)
print('Values that not equal to 3:', x != 3)
print('Values that are equal to 3:', x == 3)

# It is also possible to do an element-by-element comparison of two arrays, and 
# to include compound expressions:

print('Comparing 2x and x^2:', (2 * x) == (x ** 2))

# As in the case of arithmetic operators, the comparison operators are 
# implemented as ufuncs in NumPy. Comparison operators and their equivalent 
# ufunc are given below:
# =============================================================================
# ==    np.equal
# !=    np.not_equal
# <     np.less
# <=    np.less_equal
# >     np.greater
# >=    np.greater_equal
# =============================================================================

print('Arithmetic Ufuncs on Arrays of Any Size and Shape')
rng = np.random.RandomState(0)
y = rng.randint(10, size=(3, 4))
print('y = \n', y)
print('Values that are less than 6: \n', np.less(y, 6)) 