# -*- coding: utf-8 -*-
"""
Broadcasting extends the ufuncs ability to allow a NumPy user to remove the 
need to explicitly write slow Python loops. It is commonly used in centering
data and in displaying images based on two-dimensional functions.
"""
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt


print('Centering Array Data')
X = np.random.random((10, 3))
# Computing the mean of each feature using the mean aggregate across the first
# dimension
Xmean = X.mean(0) #Axis = 0 means that the mean is taken over each column
print('Xmean = ', Xmean)
# And now we can center the X array by subtracting the mean (this is a 
# broadcasting operation)
X_centered = X - Xmean
print('Xmean = ', X_centered.mean(0))
print('')

print('Plotting a 2D Function')
# If we want to define a function z = f(x, y), broadcasting can be
# used to compute the function across the grid
# x and y have 50 steps from 0 to 5
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x) #Broadcasting operation
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5],
cmap='viridis')
plt.colorbar();