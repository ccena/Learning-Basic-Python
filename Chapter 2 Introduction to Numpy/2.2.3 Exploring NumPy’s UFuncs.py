# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:20:20 2020

@author: HOTs
"""
import numpy as np
from scipy import special

# NumPy’s ufuncs feel very natural to use because they make use of Python’s 
# native arithmetic operators.

print('Array Arithmetic')
x = np.arange(4)
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) # floor division
print("-x = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2 = ", x % 2) #modulo
print('')

#Numpy understands Python’s built-in absolute value function
print('Absolute Value')
a = np.array([-2, -1, 0, 1, 2])
b = abs(a)
print('Using abs() method:', b)
c = np.absolute(a)
print('Using np.absolute:', c)
print('')

#Absolute value returns the magnitude of a complex data
print('Magnitude of a Vector')
d = np.array([3 - 6j, 4 - 3j, 2 + 0j, 0 + 1j]) 
e = np.abs(d) # calculates the magnitude of each vector component
print(e)
print('')

#NumPy provides a large number of useful ufuncs, and some of the most useful 
# for the data scientist are the trigonometric functions.
print('Trigonometric Functions')
theta = np.linspace(0, np.pi, 5)
print("theta = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
print('')

#One can also use inverse trigonometric functions in Numpy
print('Inverse Trigonometric Functions')
f = [-1, 0, 1]
print("f = ", f)
print("arcsin(f) = ", np.arcsin(f))
print("arccos(f) = ", np.arccos(f))
print("arctan(f) = ", np.arctan(f))
print('')

#Exponents and Logarithmic operations are available in Numpy
print('Exponents and logarithms')
g = [1, 2, 3, 4, 10]
print("g =", g)
print("e^g =", np.exp(g))
print("2^g =", np.exp2(g))
print("3^g =", np.power(3, g))
print("ln(g) =", np.log(g))
print("log2(g) =", np.log2(g))
print("log10(g) =", np.log10(g))
#Special versions of log and exponents for small values
h = [0, 0.001, 0.01, 0.1]
print("Special case: exp(h) - 1 =", np.expm1(h)) #Applies to small inputs
print("Special case: log(1 + h) =", np.log1p(h)) #Applies to small inputs
print('')

#Another excellent source for more specialized and obscure ufuncs 
# is the submodule scipy.special
print('Gamma functions (generalized factorials) and related functions')
i = [1, 5, 10]
print("gamma(i) =", special.gamma(i)) #Gamma function
print("ln|gamma(i)| =", special.gammaln(i))
print("beta(i, 2) =", special.beta(i, 2)) #Beta function
print('')

print('Error function (integral of Gaussian) its complement, and its inverse')
j = np.array([0, 0.3, 0.7, 1.0])
print("erf(j) =", special.erf(j)) 
print("erfc(j) =", special.erfc(j))
print("erfinv(j) =", special.erfinv(j))