# -*- coding: utf-8 -*-
"""
Concatenating and Splitting Arrays
"""
import numpy as np

"""Concatenation, or joining of two arrays in NumPy, is primarily accomplished
through the routines np.concatenate, np.vstack, and np.hstack."""

print('Using np.concatenate for two or more arrays:')
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
con1 = np.concatenate([x, y])
print(con1)
print('\n')
z = [100, 300, 200]
con2 = np.concatenate([x, y, z])
print(con2)
print('\n')

print('Using np.concatenate for two or more arrays:')
grid = np.array([[1, 2, 3],[4, 5, 6]])
print(grid)
print('\n')
con3 = np.concatenate([grid, grid])
print(con3)
print('\n')

print('Using np.concatenate along the second axis:')
con4 = np.concatenate([grid, grid], axis=1)
print(con4)
print('\n')


print('Using np.vstack for vertical stacking of mixed dimension arrays:')
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],[6, 5, 4]])
stack1 = np.vstack([x, grid]) #stacks the two arrays vertically
print(stack1)
print('\n')

print('Using np.hstack for horizontal stacking of mixed dimension arrays:')
y = np.array([[10],[10]])
stack2 = np.hstack([grid, y])
print(stack2)
print('\n')

"""Splitting of arrays in NumPy, is primarily implemented by the functions
np.split, np.hsplit, and np.vsplit"""
print('Using np.split to split arrays:')
k = [1, 2, 3, 99, 99, 3, 2, 1]
k1, k2, k3 = np.split(k, [3, 5])
print(k1, k2, k3)
print('\n')

print('Using np.vsplit to split arrays:')
grid2 = np.arange(16).reshape((4, 4))
print(grid2) 
print('\n')
upper, lower = np.vsplit(grid2, [2])
print('upper=\n', upper)
print('\n')
print('lower=\n', lower)
print('\n')


print('Using np.hsplit to split arrays:')
left, right = np.hsplit(grid2, [2])
print('left=\n', left)
print('\n')
print('right=\n', right)


