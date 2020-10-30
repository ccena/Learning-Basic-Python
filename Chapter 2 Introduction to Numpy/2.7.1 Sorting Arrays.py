# -*- coding: utf-8 -*-
"""
Up to this point we have been concerned mainly with tools to access and operate 
on array data with NumPy. This section covers algorithms related to sorting 
values in NumPy arrays. 
"""


import numpy as np

def selection_sort(x):
    """
    A simple selection sort repeatedly finds the minimum value 
    from a list, and makes swaps until the list is sorted.
    """
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2, 1, 4, 3, 5])
print(selection_sort(x))


def bogosort(x):
    """
    This method relies on pure chance: it repeatedly applies a random shuffling
    of the array until the result happens to be sorted.
    """
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

x = np.array([2, 1, 4, 3, 5])
print(bogosort(x))


# Fortunately, Python contains built-in sorting algorithms that are much more 
# efficient than either of the simplistic algorithms just shown. We’ll start by 
# looking at the Python built-ins, and then take a look at the routines 
# included in NumPy and optimized for NumPy arrays