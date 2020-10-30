# -*- coding: utf-8 -*-
"""
A simple histogram can be a great first step in understanding a dataset. 
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

# =============================================================================
#                               Histograms
# =============================================================================
data = np.random.randn(1000)
plt.hist(data)
plt.title("Simple Histogram")

# Options in a hist() function to tune both the calculation and the display
plt.figure()
plt.hist(data, bins=30, density=True, alpha=0.8,
         histtype='stepfilled', color='steelblue',
         edgecolor='none');

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype='stepfilled', alpha=0.5, density=True, bins=40)
plt.hist(x1, **kwargs, color='red')
plt.hist(x2, **kwargs, color='yellow')
plt.hist(x3, **kwargs, color='green');
plt.title("Comparing histograms of several distributions")

# If you would like to simply compute the histogram (that is, count the number 
# of points in a given bin) and not display it, the np.histogram() function
counts, bin_edges = np.histogram(data, bins=10)
print(counts)

# =============================================================================
#                    Two-Dimensional Histograms and Binnings
# =============================================================================

# Defining x and y array drawn from a multivariate Gaussian distribution
plt.figure()
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T #Transpose

# Use plt.hist2d for Two-dimensional histogram
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
plt.title("A two-dimensional histogram with plt.hist2d")
# plt.hist2d has a counterpart in np.histogram2d
counts, xedges, yedges = np.histogram2d(x, y, bins=30)

# Use plt.hexbin for Hexagonal binnings
# plt.hexbin has a number of interesting options, including the ability to
# specify weights for each point, and to change the output in each bin to any
# NumPy aggregate (mean of weights, standard deviation of weights, etc.).
plt.figure()
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
plt.title("A two-dimensional histogram with plt.hexbin")

# Evaluate densities in multiple dimensions using Kernel density estimation
from scipy.stats import gaussian_kde
# fit an array of size [Ndim, Nsamples]
data = np.vstack([x, y])
kde = gaussian_kde(data)
# evaluate on a regular grid
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
#Applying KDE on the data
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))
# Plot the result as an image
plt.figure()
plt.imshow(Z.reshape(Xgrid.shape),
origin='lower', aspect='auto',
extent=[-3.5, 3.5, -6, 6],
cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")
plt.title("Kernel Density Estimation")


