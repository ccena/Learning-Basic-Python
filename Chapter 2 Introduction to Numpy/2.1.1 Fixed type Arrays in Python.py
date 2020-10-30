# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:51:25 2020
Python offers several different options for storing data in efficient, 
fixed-type data buffers. The built-in array module can be used to create
dense arrays of a uniform type
@author: HOTs
"""
#Creating a Simple Array
import array
L = list(range(10))
A = array.array('i', L)
print(A)