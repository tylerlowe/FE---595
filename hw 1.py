import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2*np.pi)
sine = np.sin(x)
cosine = np.cos(x)
tangent = np.tan(x)

plt.plot(x, sine)
plt.plot(x, cosine)
plt.plot(x, tangent)
plt.show()
