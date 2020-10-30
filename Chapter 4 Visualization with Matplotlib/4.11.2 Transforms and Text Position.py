# -*- coding: utf-8 -*-
"""
Sometimes
it’s preferable to anchor the text to a position on the axes or figure, 
independent of the data. In Matplotlib, we do this by modifying the transform.
ax.transData
        Transform associated with data coordinates
ax.transAxes
        Transform associated with the axes (in units of axes dimensions)
fig.transFigure
        Transform associated with the figure (in units of figure dimensions)
"""
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])
# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);
fig

# If we change the axes limits, it is only the transData coordinates that
# will be affected, while the others remain stationary
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);
ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
