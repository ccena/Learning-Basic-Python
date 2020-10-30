# -*- coding: utf-8 -*-
"""
A potentially confusing feature of Matplotlib is its dual interfaces: 
(1) a convenient MATLAB-style state-based interface, 
and (2) a more powerful object-oriented interface.
"""

import matplotlib.pyplot as plt
import numpy as np



#Object-Oriented (OO) Style
x = np.linspace(0, 2, 100)
#Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots() # Create a figure and an axes.
#Create the plots with labels, different line colors, and styles
ax.plot(x, x, label='linear', color='blue', 
        linestyle='dashdot') # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic', color='0.75', 
        linestyle='-') # Plot more data on the axes...
ax.plot(x, x**3, label='cubic', color='#FFDD44', 
        linestyle='--') # ... and some more.
#Label the plot
ax.set_xlabel('x label') # Add an x-label to the axes.
ax.set_ylabel('y label') # Add a y-label to the axes.
ax.set_title("Simple Plot in OO Style") # Add a title to the axes.
ax.legend() # Add a legend.


#MATLAB Style
x = np.linspace(0, 2, 100)
plt.figure()
plt.plot(x, x, label='linear', color='chartreuse', 
        linestyle=':') # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic', color = 'red',
         linestyle = 'dotted') # etc.
plt.plot(x, x**3, label='cubic', color = 'pink',
         linestyle = 'solid')
#Labelling the plot
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot in MATLAB Style")
plt.legend()




