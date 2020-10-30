# -*- coding: utf-8 -*-
"""
The plt.plot() command is able to
create multiple lines at once, and returns a list of created line instances. 
Passing any of these to plt.legend() will tell it which to identify, along 
with the labels we’d like to specify.
"""
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

#A cleaner approach
#lines is a list of plt.Line2D instances
plt.legend(lines[:4], ['first', 'second', 'third', 'fourth']);
plt.title("Customization of legend elements")

#A more messy approach 
plt.figure()
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True);
plt.title("Alternative method of customizing legend elements")