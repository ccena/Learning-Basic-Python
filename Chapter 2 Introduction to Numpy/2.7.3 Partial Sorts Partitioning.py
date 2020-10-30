# -*- coding: utf-8 -*-
"""
Sometimes we’re not interested in sorting the entire array, but simply want to
find the K smallest values in the array.
NumPy provides this in the np.partition function which takes an array and a 
number K; the result is a new array with the smallest K values to the left of 
the partition, and the remaining values to the right,in arbitrary order:
"""
import numpy as np
x = np.array([7, 2, 3, 1, 6, 5, 4])
print('Array: ', x)
print('First 3 Slots with the Smallest Values: ', np.partition(x, 3))
# Note that the first three values in the resulting array are the three 
# smallest in the array, and the remaining array positions contain the
# remaining values.
print('')
# Similarly to sorting, we can partition along an arbitrary axis of a
# multidimensional array
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print('Array:\n', X)
print('First 2 Slots in a Row with the Smallest Values:\n', 
      np.partition(X, 2, axis=1))