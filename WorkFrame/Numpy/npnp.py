import numpy as np
import matplotlib.pyplot as plt
points= np.arange(-5,5,0.01)
xs, ys = np.meshgrid(points, points)
ys

z = np.sqrt(xs**2+ys**2)

plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
plt.show()


