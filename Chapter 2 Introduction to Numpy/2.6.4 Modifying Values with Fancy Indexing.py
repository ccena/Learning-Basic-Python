# -*- coding: utf-8 -*-
"""
Just as fancy indexing can be used to access parts of an array, it can also be 
used to modify parts of an array.
"""
import numpy as np

x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99 #The elements accessed by i is changed to 99
print(x)
x[i] -= 10 #The elements accessed by i is subtracted by 10
print(x)

# Notice, though, that repeated indices with these operations can cause some 
# potentially unexpected results. Consider the following:
y = np.zeros(10)
y[[0, 0]] = [4, 6]
print(y)
# Where did the 4 go? The result of this operation is to first assign x[0] = 4,
# followed by x[0] = 6. The result, of course, is that x[0] contains the value 
# 6.
j = [2, 3, 3, 4, 4, 4]
y[j] += 1 #The equation, x[i] = x[i] + 1 is evaluated, and then the result is 
# assigned to the indices in x multiple times, hence x[4] += 1 is just 1 not 3. 
print(y)

# In order to repeat the operation, one can use the at() method of ufuncs
y = np.zeros(10)
np.add.at(y, j, 1)
print(y)

# The at() method does an in-place application of the given operator at the 
# specified indices (here, i) with the specified value (here, 1). Another method 
# that is similar in spirit is the reduceat() method of ufuncs, which you can 
# read about in the NumPy documentation.