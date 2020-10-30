# -*- coding: utf-8 -*-
"""
Matplotlib has a very convenient style module, which includes a number of new 
default stylesheets, as well as the ability to create and package your own 
styles.
The basic way to switch to a stylesheet is to call:
 plt.style.use('stylename')
 Some Style Choices:
        'fivethirtyeight',
        'seaborn-pastel',
        'seaborn-whitegrid',
        'ggplot',
        'grayscale'             
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.style.use('classic')

# Create a function that makes histograms and line plots
def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')
    
# Calling the Function
hist_and_lines()

# FiveThirtyEight style
with plt.style.context('fivethirtyeight'):
    hist_and_lines()
    
# ggplot
with plt.style.context('ggplot'):
    hist_and_lines()    
    
# Bayesian Methods for Hackers style
with plt.style.context('bmh'):
    hist_and_lines()

# Dark background
with plt.style.context('dark_background'):
    hist_and_lines()

# Grayscale
with plt.style.context('grayscale'):
    hist_and_lines()

import seaborn as sns
sns.set_style("darkgrid")
hist_and_lines()
