# -*- coding: utf-8 -*-
"""
Seaborn provides an API on top of Matplotlib
that offers sane choices for plot style and color defaults, defines simple 
high-level functions for common statistical plot types, and integrates with the 
functionality provided by Pandas DataFrames.
"""

import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np


# Seaborn Versus Matplotlib
# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
plt.title("Data in Matplotlib’s default style")


import seaborn as sns
sns.set()
plt.figure()
# same plotting code as above!
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
plt.title("Data in Seaborn’s default style")

