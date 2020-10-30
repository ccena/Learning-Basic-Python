# -*- coding: utf-8 -*-
"""
Matplotlib graphs your data on Figures (i.e., windows, Jupyter widgets, etc.),
each of which can contain one or more Axes (i.e., an area where points can be 
specified in terms of x-y coordinates (or theta-r in a polar plot, or x-y-z in
a 3D plot, etc.). One of Matplotlib’s most important features is its ability to 
play well with many operating systems and graphics backends.
"""

# =============================================================================
#                        'GENERAL MATPLOTLIB TIPS'
# =============================================================================

#importing matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#setting styles
plt.style.use('classic')

#plotting from script
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
# plt.show() command should be used only once per Python session,
plt.show()

#saving figures to file
fig.savefig('my_figure.png')

    
