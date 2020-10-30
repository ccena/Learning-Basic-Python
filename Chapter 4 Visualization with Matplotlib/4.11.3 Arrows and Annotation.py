# -*- coding: utf-8 -*-
"""
The plt.annotate() function creates some text and an arrow, and 
the arrows can be very flexibly specified. In an annotation, there are two 
points to consider: the location being annotated represented by the argument 
xy and the location of the text xytext. Both of these arguments are (x, y) 
tuples.
"""
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


#OO style
fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            arrowprops=dict(arrowstyle="->",
                connectionstyle="angle3,angleA=0,angleB=-90"));
plt.show()


#MATLAB style
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
arrowprops=dict(facecolor='black', shrink=0.05))
plt.ylim(-2, 2)
