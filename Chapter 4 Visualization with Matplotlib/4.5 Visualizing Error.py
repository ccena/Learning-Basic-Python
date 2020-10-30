# -*- coding: utf-8 -*-
"""
For any scientific measurement, accurate accounting for errors is nearly as 
important, if not more important, than accurate reporting of the number itself.
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# Create Basic Error Bars
x = np.linspace(0, 10, 50) 
dy = 0.8 # Error of measurement
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.k') # Errorbar plot with black ('k')
# Note: fmt is a format code controlling the appearance of lines and points

# Finetune the output using the errorbar function
plt.figure()
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
              ecolor='lightgray', elinewidth=3, capsize=0);
