# -*- coding: utf-8 -*-
"""
Plot legends identify discrete labels of discrete points. For continuous labels 
based on the color of points, lines, or regions, a labeled colorbar can be a 
great tool.
"""


import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

#Creating a simple color bar
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
plt.imshow(I) #Creates a continuous image
plt.colorbar(); #Adds the colorbar
plt.title("A simple colorbar legend")

# =============================================================================
#                           Customizing colorbars
# =============================================================================
from matplotlib.colors import LinearSegmentedColormap
def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]
    return LinearSegmentedColormap.from_list(cmap.name + "_gray",
                                             colors, cmap.N)

def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))
    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
    
view_colormap('jet')
plt.title("The jet colormap and its uneven luminance scale")
view_colormap('viridis')
plt.title("The viridis colormap and its even luminance scale")
view_colormap('cubehelix')
plt.title("The cubehelix colormap and its luminance")
view_colormap('RdBu')
plt.title("The RdBu (Red-Blue) colormap and its luminance")

# =============================================================================
#                       Color limits and extensions
# =============================================================================
# make noise in 1% of the image pixels
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
plt.figure(figsize=(10, 3.5))
plt.subplot(1, 2, 1)
plt.imshow(I, cmap='RdBu')
plt.colorbar()
plt.subplot(1, 2, 2)
plt.imshow(I, cmap='RdBu')
plt.colorbar(extend='both')
plt.clim(-1, 1);
plt.title("Specifying colormap extensions")

# =============================================================================
#                            Discrete colorbars
# =============================================================================
# The easiest way to represent discrete values in a colormap is to use 
# the plt.cm.get_cmap() function, and pass the name of a suitable colormap 
# along with the number of desired bins
plt.figure()
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1);

