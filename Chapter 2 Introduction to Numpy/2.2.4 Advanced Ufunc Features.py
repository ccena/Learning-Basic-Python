# -*- coding: utf-8 -*-
"""
Numpy has a few specialized features, such as specifying the output, 
aggregates, and Outer products.
"""
import numpy as np

# For large calculations, Ufunc is able to specify the array where the result
# of the calculation will be stored. 

print('Specifying the Output Using "out =\" Argument ' )
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print('y= ', y)
z = np.zeros(10)
np.power(2, x, out=z[::2])
print('z= ', z)
print('')

# For binary ufuncs, there are some interesting aggregates that can be computed
# directly from the object.
print('Aggregates using "reduce method\"')
a = np.arange(1, 6)
print(a)
#Using reduce repeatedly applies a given operation to the elements of an array 
#until only a single result remains.
print('Reduced array via addition: ', np.add.reduce(a)) 
print('Reduced array via multiplication: ', np.multiply.reduce(a)) 
print('')
#Once can also store all the intermediate results of the computation
print('Aggregates using "accumulate method\"')
print('Accumulated array via add.accumulate: ', np.add.accumulate(a))
print('Accumulated array via multiply.accumulate: ', np.multiply.accumulate(a))
print('')

# Any ufunc can compute the output of all pairs of two different inputs using
# the outer method
print('Outer Products ')
b = np.arange(1, 6)
print(np.multiply.outer(b, b)) #Similar to a multiplication table
