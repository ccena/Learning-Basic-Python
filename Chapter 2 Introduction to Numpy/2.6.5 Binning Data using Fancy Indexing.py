# -*- coding: utf-8 -*-
"""
You can use Fancy Indexing to efficiently bin data to create a histogram by 
hand. For example, imagine we have 1,000 values and would like to quickly find 
where they fall within an array of bins.
"""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
# find the appropriate bin for each x
i = np.searchsorted(bins, x, side = 'right')
# add 1 to each of these bins
np.add.at(counts, i, 1)
# The counts now reflect the number of points within each bin—in other words, 
# a histogram
# plot the results
plt.plot(bins, counts, linestyle='steps');

# Such results can be obtained by using Matplotlib histogram.
plt.hist(x, bins, histtype='step');
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins) #20.5 us
print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1) #10.6 us
# The custom one-line algorithm is several times faster than the optimized 
# algorithm in NumPy!
print('')

x = np.random.randn(1000000)
print("NumPy routine:") 
%timeit counts, edges = np.histogram(x, bins) #48.6 ms
print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1) #

# =============================================================================
# An algorithm efficient for large datasets will not always be the best choice
# for small datasets, and vice versa
# =============================================================================
