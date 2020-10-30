# -*- coding: utf-8 -*-
"""
Plot legends give meaning to a visualization, assigning labels to the various 
plot elements. 
The simplest legend can be created with the plt.legend() 
command, which automatically creates a legend for any labeled plot elements.
"""

import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.linspace(0, 10, 1000)
plt.figure()
plt.plot(x, np.sin(x), '-b', label='Sine')
plt.plot(x, np.cos(x), '--r', label='Cosine')
plt.axis('equal')
leg = plt.legend();
plt.title("A default plot legend")

# Customize the legend
plt.figure()
plt.plot(x, np.sin(x), '-b', label='Sine')
plt.plot(x, np.cos(x), '--r', label='Cosine')
plt.axis('equal')
plt.legend(loc='upper left', frameon=False);#if frameon=True, add an outline
plt.title("A customized plot legend")

# Specifying the number of columns in the legend with the ncol command
plt.figure()
plt.plot(x, np.sin(x), '-b', label='Sine')
plt.plot(x, np.cos(x), '--r', label='Cosine')
plt.axis('equal')
plt.legend(frameon=False, loc='lower center', ncol=2) #A legend of 2 columns
plt.title("A two-column plot legend")

# add a shadow, change the transparency (alpha value) of the frame, or
# change the text padding with fancybox
plt.figure()
plt.plot(x, np.sin(x), '-b', label='Sine')
plt.plot(x, np.cos(x), '--r', label='Cosine')
plt.axis('equal')
plt.legend(fancybox=True, framealpha=0.6, shadow=True, borderpad=1)
plt.title("A fancybox plot legend")