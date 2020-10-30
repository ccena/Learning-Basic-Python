# -*- coding: utf-8 -*-
"""
Although Python has built-in sort and sorted functions to work with lists, 
NumPy’s np.sort function turns out to be much more efficient and useful for 
our purposes. By default np.sort uses an O(N log N) , quicksort algorithm, 
though mergesort and heapsort are also available. For most applications, the 
default quicksort is more than sufficient.
"""

import numpy as np

# To return a sorted version of the array without modifying the input, you 
# can use np.sort:
    
x = np.array([2, 1, 4, 3, 5])
print('Array:', x)
print('Sorted Array using np.sort(x):', np.sort(x))

# If you prefer to sort the array in-place, you can instead use the sort method
# of arrays.
x.sort()
print('Sorted Array using .sort():', x)

# A related function is argsort, which instead returns the indices of the 
# sorted elements:
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print('Indices of the Sorted Elements: ', i)
print('Sorted Array using the indices: ', x[i])
print('')

print('Sorting along rows or columns')
# A useful feature of NumPy’s sorting algorithms is the ability to sort along 
# specific rows or columns of a multidimensional array using the axis argument
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print('Array: \n', X)
print('Sorting each colum of X: \n', np.sort(X, axis=0))
print('Sorting each row of X: \n', np.sort(X, axis=1))
# Keep in mind that this treats each row or column as an independent array, 
# and any relationships between the row or column values will be lost!


