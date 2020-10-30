# -*- coding: utf-8 -*-
"""
The default implementation of Python does some operations very
slowly especially in situations where
many small operations are being repeated—for instance, looping over arrays to
to operate on each element.
"""
import numpy as np
np.random.seed(0)

"""An Example of Slowness of Loops"""
def compute_reciprocals(values):
	output = np.empty(len(values))
	for i in range(len(values)):
		output[i] = 1.0 / values[i]
	return output

values = np.random.randint(1, 10, size=5)
big_array = np.random

#Understanding the Slowness in Operating Arrays
print('Calculation Times using Functions:')
%timeit compute_reciprocals(values) #slow operation, 9.11 µs ± 288 ns per loop
%timeit compute_reciprocals(big_array) #slow operation, 1.69s ± 23.5ms per loop
print('')
print('Calculation Times using UFunctions:')
%timeit 1.0 / values # fast operation, 956 ns ± 54.7 ns per loop
%timeit 1.0 / big_array # fast operation, 3.65 ms ± 65.5 µs per loop
print('')

