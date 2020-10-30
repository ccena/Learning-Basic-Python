# -*- coding: utf-8 -*-
"""
Matplotlib’s default tick locators and formatters are designed to be generally 
sufficient in many common situations, but are in no way optimal for every plot. 
This section will give several examples of adjusting the tick locations and 
formatting for the particular plot type you’re interested in
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# Major and Minor Ticks
ax = plt.axes(xscale='log', yscale='log')
print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())
print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

#Hiding Ticks or Labels
plt.figure()
ax = plt.axes()
ax.plot(np.random.rand(50))
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

plt.figure()
fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)
# Get some face data from scikit-learn
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces().images
for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")
        
        
#Reducing or Increasing the Number of Ticks
# plt.MaxNLocator(), which allows us to specify the maximum number of ticks 
# that will be displayed
fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
# For every axis, set the x and y major locator
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(4))
    axi.yaxis.set_major_locator(plt.MaxNLocator(4))
fig 