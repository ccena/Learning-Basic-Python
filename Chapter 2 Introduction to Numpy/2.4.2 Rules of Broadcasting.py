# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:24:45 2020
• Rule 1: If the two arrays differ in their number of dimensions, the shape of 
the one with fewer dimensions is padded with ones on its leading (left) side.

• Rule 2: If the shape of the two arrays does not match in any dimension, the 
array with shape equal to 1 in that dimension is stretched to match 
the other shape.

• Rule 3: If in any dimension the sizes disagree and neither is equal to 1, 
an error is raised.
"""
import numpy as np

# =============================================================================
# Example 1
# =============================================================================
M = np.ones((2, 3))
a = np.arange(3)
print('M size =', M.shape) 
print('a size =', a.shape) 

# =============================================================================
# Rule 1: the one with fewer dimensions is padded with ones on its leading 
# (left) side. Here, array 'a' has fewer dimensions so we pad 'a'.
# M.shape -> (2, 3)
# a.shape -> (1, 3) Shape after Padding
# Rule 2: the array with shape equal to 1 in that dimension is stretched to
# match the other shape. By streching 'a', both arrays now have the same size
# # M.shape -> (2, 3)
# # a.shape -> (2, 3) 
# =============================================================================
print('M + a = \n', M + a)
print('')
# =============================================================================
# Example 2
# =============================================================================
c = np.arange(3).reshape((3, 1))
d = np.arange(3)
print('c size =', c.shape) 
print('d size =', d.shape) 
# =============================================================================
# Rule 2: the one with fewer dimensions is padded with ones on its leading 
# (left) side. Here, array 'd' has fewer dimensions so we pad 'd'.
# a.shape -> (3, 1)
# b.shape ->  (1, 3) Shape after Padding
# Rule 2: upgrade each of these ones to match the corresponding
# size of the other array
# a.shape -> (3, 3)
# b.shape -> (3, 3)
# =============================================================================
print('c + d = \n', c + d)
print('')

# =============================================================================
# Example 3
# =============================================================================
e = np.ones((3, 2))
f = np.arange(3)
print('e size =', e.shape) 
print('f size =', f.shape) 
# =============================================================================
# Rule 3: the one with fewer dimensions is padded with ones on its leading 
# (left) side. Here, array 'd' has fewer dimensions so we pad 'd'.
# e.shape -> (3, 2)
# f.shape -> (1, 3) Shape after Padding
# Rule 2: the first dimension of f is stretched to match that of e:
# e.shape -> (3, 3)
# f.shape -> (3, 3) Rule 3: the final shapes do not match, so these two arrays
 # are incompatible.
# =============================================================================



