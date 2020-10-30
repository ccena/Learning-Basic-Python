# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:52:36 2020
Especially for larger arrays, it is more efficient to create arrays from 
scratch using routines built into NumPy.
"""
import numpy as np
# Create a length-10 integer array filled with zeros
zero_array = np.zeros(10, dtype=int)
print(zero_array)
print('\n')

# Create a 3x5 floating-point array filled with 1s
one_array = np.ones((3, 5), dtype=float)
print(one_array)
print('\n')

# Create a 3x5 array filled with 3.14
full_array = np.full((3,5), 3.14)
print(full_array)
print('\n')

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
arange_array = np.arange(0, 20, 2)
print(arange_array)
print('\n')

# Create an array of five values evenly spaced between 0 and 1
linspace_array = np.linspace(0, 6, 5)
print(linspace_array)
print('\n')

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
random_array = np.random.random((4, 4))
print(random_array)
print('\n')

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
random_normal_array = np.random.normal(0, 1, (3, 3))
print(random_normal_array)
print('\n')

# Create a 3x3 array of random integers in the interval [0, 10)
randint_array = np.random.randint(0, 10, (3, 3))
print(randint_array)
print('\n')

# Create a 3x3 identity matrix
identity_array = np.eye(3)
print(identity_array)
print('\n')

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location
uninit_array = np.empty(3)
print(uninit_array)
print('\n')


