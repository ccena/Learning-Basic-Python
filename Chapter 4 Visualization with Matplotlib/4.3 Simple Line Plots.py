# -*- coding: utf-8 -*-
"""
The simplest of all plots is the visualization of a single function y = f(x)
"""


import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 1000)
plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
#Adjusting the axes limits
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5) #for simplicity, plt.axis([-1, 11, -1.5, 1.5]) can be used
plt.axis('equal') #ensuring an equal aspect ratio of the x and y axis


#Adjusting the line color and style of the plot
plt.figure()
plt.plot(x, np.sin(x - 0), color='blue') # specify color by name
plt.plot(x, np.sin(x - 1), color='g') # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75') # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 and 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); #all HTML color names supported

#Adjusting the line style using the linestyle keyword
plt.figure()
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');
# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-') # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':'); # dotted


