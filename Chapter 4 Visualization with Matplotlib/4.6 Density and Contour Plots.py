# -*- coding: utf-8 -*-
"""
Sometimes it is useful to display three-dimensional data in two dimensions 
using contours or color-coded regions. There are three Matplotlib functions 
that can be helpful for this task: plt.contour for contour plots, plt.contourf 
for filled contour plots, and plt.imshow for showing images.
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

# =============================================================================
#                   Visualizing a Three-Dimensional Function
# =============================================================================

# Create a contour plot using a function z = f(x, y)
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black')
plt.title("Basic Contour"); # Input: grid of x, y, z values
# Notice that by default when a single color is used, negative values are 
# represented by dashed lines, and positive values by solid lines.

# Color-code the lines of the plot by using a cmap argument
plt.figure()
plt.contour(X, Y, Z, 20, cmap='RdGy'); # Adding 20 equally spaced intervals
plt.title("Coloured Contour")

# Create a filled contour plot using the plt.contourf() function
plt.figure()
plt.contourf(X, Y, Z, 20, cmap='RdGy') # Adding 20 equally spaced intervals
plt.colorbar(); # Adding a colorbar that gives color information for the plot
plt.title("Filled Contour")

# Create a continuous image of the contour plot with plt.imshow()
plt.figure()
# imshow only accepts values min and max values of x and y
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy')
plt.colorbar()
plt.title("Image of the Contour")
plt.axis(aspect='image');

# Combining contour maps and image plots
plt.figure()
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)
plt.title("Overlayed Image over a Contour")
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
cmap='RdGy', alpha=0.5)
plt.colorbar();

# The combination of these three functions—plt.contour, plt.contourf, and
# plt.imshow—gives nearly limitless possibilities for displaying this sort of 
# threedimensional data within a two-dimensional plot.
