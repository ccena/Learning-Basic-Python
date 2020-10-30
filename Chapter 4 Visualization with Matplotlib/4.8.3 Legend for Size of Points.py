# -*- coding: utf-8 -*-
"""
Sometimes the legend defaults are not sufficient for the given visualization.
Perhaps you’re using the size of points to mark certain features of the data, 
and want to create a legend reflecting this.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cities = pd.read_csv('california_cities.csv')
# Extract the data we're interested in
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), 
            cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=area,label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, title='City Area')
plt.title('California Cities: Area and Population');