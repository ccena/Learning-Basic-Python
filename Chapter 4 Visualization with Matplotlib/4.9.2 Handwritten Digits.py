# -*- coding: utf-8 -*-
"""
let’s look at an interesting visualization of some handwritten digits data. 
This data is included in Scikit-Learn, and consists of
nearly 2,000 8×8 thumbnails showing various handwritten digits.
"""


import matplotlib.pyplot as plt


from sklearn.datasets import load_digits
digits = load_digits(n_class=6)
fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

# project the digits into 2 dimensions using IsoMap
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)
    
# plot the results
plt.figure()
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
plt.colorbar(ticks=range(6), label='digit value')
plt.clim(-0.5, 5.5)
plt.title("Manifold embedding of handwritten digit pixels")