# -*- coding: utf-8 -*-
"""
Matplotlib has the concept of subplots: groups of smaller axes that can exist 
together within a single figure. These subplots might be insets, grids of 
plots, or other more complicated layouts.
"""
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

# =============================================================================
#                       plt.axes: Subplots by Hand
# =============================================================================
#This is a very complicated way of creating a subplot
ax1 = plt.axes() # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
ylim=(-1.2, 1.2))
x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x));

# =============================================================================
#                   plt.subplot: Simple Grids of Subplots
# =============================================================================
#plt.subplot() creates a single subplot within a grid and takes three values:
#the number of rows, the number of columns, and the index of the plot
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')   
    
#plt.subplots_adjust can be used to adjust the spacing between these plots
#for OO style, one can use fig.add_subplot()
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
            fontsize=18, ha='center')
    
# =============================================================================
#                       plt.subplots: The Whole Grid in One Go
# =============================================================================
# With sharex and sharey, we’ve automatically removed inner labels on the grid
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# axes are in a two-dimensional array, indexed by [row, col]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
              fontsize=18, ha='center')
fig
# In comparison to plt.subplot(), plt.subplots() is more consistent with
# Python’s conventional 0-based indexing.

# =============================================================================
#                    plt.GridSpec: More Complicated Arrangements
# =============================================================================
# plt.GridSpec() is the best tool in going beyond a regular grid to subplots 
# that span multiple rows and columns
fig = plt.figure()
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2]);

# Create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T
# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)
# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
orientation='vertical', color='gray')
x_hist.invert_yaxis()
y_hist.hist(y, 40, histtype='stepfilled',
orientation='horizontal', color='gray')
y_hist.invert_xaxis()



