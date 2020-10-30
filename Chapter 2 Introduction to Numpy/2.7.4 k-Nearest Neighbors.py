# -*- coding: utf-8 -*-
"""
The function np.argpartition computes indices of the partition.
Let’s quickly see how we might use this argsort function along multiple axes 
to find the nearest neighbors of each point in a set. We’ll start by creating
a random set of 10
"""

import numpy as np

X = np.random.rand(10, 2)
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling
plt.scatter(X[:, 0], X[:, 1], s=100);
# Now we’ll compute the distance between each pair of points. Recall that the 
# squareddistance between two points is the sum of the squared differences in 
# each dimension.
dist_sq = np.sum((X[:,np.newaxis,:] - X[np.newaxis,:,:]) ** 2, axis=-1)

# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
print(differences.shape)
# square the coordinate differences
sq_differences = differences ** 2
print(sq_differences.shape)
# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
print(dist_sq.shape)
print(dist_sq.diagonal())
print('')
nearest = np.argsort(dist_sq, axis=1)
print(nearest)

K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
plt.scatter(X[:, 0], X[:, 1], s=100)
# draw lines from each point to its two nearest neighbors
K = 2
for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')