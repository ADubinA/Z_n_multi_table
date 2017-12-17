
import numpy as np
import scipy.ndimage as sp
import matplotlib.pyplot as plt


def multiplication_table(n, color='jet'):
    arr = np.fromfunction(lambda i, j: (i+1)*(j+1) % n, (n-1, n-1))
    arr = sp.filters.gaussian_filter(arr, 0.4)
    c_map = plt.cm.get_cmap(color)
    _, ax = plt.subplots()
    ax.imshow(arr, interpolation='nearest', cmap=c_map, vmin=1)


multiplication_table(2000)
plt.show()
