# -*- coding: utf-8 -*-
"""
Another commonly used plot type is the simple scatter plot, a close cousin of 
the line plot. Instead of points being joined by line segments, here the points 
are represented individually with a dot, circle, or other shape.

Two Methods: (1) plt.plot and (2) plt.scatter
(a) plt.plot can be noticeably more efficient than plt.scatter since the latter
uses a renderer that takes up memory. 
(b) plt.plot should be preferred over plt.scatter for large datasets
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# =============================================================================
#                       Scatter Plots with plt.plot
# =============================================================================
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.figure()
plt.plot(x, y, 'o', color='black');
plt.show()

# The full list of available marker styles
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd', 'p']:
        plt.plot(rng.rand(5), rng.rand(5), marker,
                 label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);   

# Combine character codes together with line and color codes
plt.figure()
plt.plot(x, y, '-ok'); # line (-), circle marker (o), black (k)

# Specify a wide range of properties of the lines and markers
plt.figure()
plt.plot(x, y, '-p', color='gray', 
         markersize=15, 
         linewidth=4,
         markerfacecolor='yellow',
         markeredgecolor='purple',
         markeredgewidth=1)
plt.ylim(-1.2, 1.2);

# =============================================================================
#                       Scatter Plots with plt.scatter
# =============================================================================

# Plt.scatter creates scatter plots where the size, face color, edge color, 
# etc are individually controlled
plt.figure()
plt.scatter(x, y, marker='o');
plt.axis([-0.5, 11, -1.2, 1.2 ] )

# Create a Plot of Different Colors and Sizes
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.figure()
# Use different colors and set transparency with apha keyword
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4, cmap='viridis')
plt.colorbar(); # show color scale

# Iris data from Scikit-Learn shows each sample as one of three types of 
# flowers that has had the size of its petals and sepals carefully measured 
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
plt.figure()
plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);  





