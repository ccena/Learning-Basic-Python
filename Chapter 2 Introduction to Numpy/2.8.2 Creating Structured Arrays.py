# -*- coding: utf-8 -*-
"""
Structured array data types can be specified in a number of ways. Earlier, 
we saw the dictionary method:
"""
import numpy as np

print('Creating Structured Arrays')
a = np.dtype({'names':('name', 'age', 'weight'),
              'formats':('U10', 'i4', 'f8')})
print('Using Dictionary Method:', a)
print('')

# For clarity, numerical types can be specified with Python types or NumPy 
# dtypes instead:
b = np.dtype({'names':('name', 'age', 'weight'),
          'formats':((np.str_, 10), int, np.float32)})  
print('Using NumPy dtypes:', b)
print('')

# A compound type can also be specified as a list of tuples:
c = np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
print('Using List of Tuples: ', c)
print('')

# If the names of the types do not matter to you, you can specify the types 
# alone in a comma-separated string.
d = np.dtype('S10,i4,f8')
print('Only Specifiying the Type : ', d)
# The first character is '<' or '>' specifies the ordering convention 
# for significant bits. 
# The next character specifies the type of data: characters, bytes, ints, 
# floating points, and soon.
# The last character or characters represents the size of the object in bytes.