# -*- coding: utf-8 -*-
"""
NumPy also provides the np.recarray class, which is almost identical to the 
structured arrays just described, but with one additional feature: fields 
can be accessed as attributes rather than as dictionary keys.
"""
import numpy as np
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]
    	
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
'formats':('U10', 'i4', 'f8')})
data['name'] = name
data['age'] = age
data['weight'] = weight
print('Data: ', data)
print('')
print('Age: ', data['age'])   
# If we view our data as a record array instead, we can access this with 
# slightly fewer keystrokes:  
data_rec = data.view(np.recarray)
print('Accessing Age using np.recarray: ', data_rec.age)

# The downside is that for record arrays, there is some extra overhead 
# involved in accessing the fields, even when using the same syntax. 
# We can see this here:
%timeit data['age']
%timeit data_rec['age']
%timeit data_rec.age
