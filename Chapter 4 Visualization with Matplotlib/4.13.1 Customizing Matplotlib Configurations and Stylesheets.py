# -*- coding: utf-8 -*-
"""
Here we’ll walk through some of Matplotlib’s runtime configuration (rc) 
options, and take a look at the newer stylesheets feature, which contains 
some nice sets of default configurations
"""


# =============================================================================
#                       Plot Customization by Hand
# =============================================================================
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.random.randn(1000)
plt.hist(x)
plt.title("A histogram in Matplotlib’s default style")
# We can adjust this by hand to make it a much more visually pleasing plot

# use a gray background
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)

# draw solid white grid lines
plt.grid(color='black', linestyle='dashed')

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

# hide top and right ticks
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')
for tick in ax.get_yticklabels():
    tick.set_color('gray')

# control face and edge color of histogram
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666')
plt.title("A histogram with manual customizations")


# =============================================================================
#                       Changing the Defaults: rcParams
# =============================================================================
from matplotlib import cycler
colors = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

# With these settings defined, we can now create a plot and see our settings 
# in action
plt.figure()
plt.hist(x)
plt.title('A customized histogram using rc settings')

# Let’s see what simple line plots look like with these rc parameters
plt.figure()
for i in range(4):
    plt.plot(np.random.rand(10))
inline_rc = dict(mpl.rcParams)