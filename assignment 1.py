import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, np.pi/16)
sine = np.sin(x)
cosine = np.cos(x)

plt.plot(x, sine)
plt.plot(x, cosine)
plt.show()
