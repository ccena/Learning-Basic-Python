# -*- coding: utf-8 -*-
"""
One common use of fancy indexing is the selection of subsets of rows from 
a matrix. For example, we might have an N by D matrix representing N points
in D dimensions,such as the following points drawn from a two-dimensional 
normal distribution:
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # for plot styling

mean = [0, 0]
cov = [[1, 2],
[2, 5]]
X = np.random.multivariate_normal(mean, cov, 100)
print(X.shape)
plt.scatter(X[:, 0], X[:, 1]);
indices = np.random.choice(X.shape[0], 20, replace=False)
print(indices)
selection = X[indices] # fancy indexing here
print(selection.shape)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
facecolor='none', s=200); 

# This sort of strategy is often used to quickly partition datasets, as is 
# often needed in train/test splitting for validation of statistical models and
# in sampling approaches to answering statistical questions.