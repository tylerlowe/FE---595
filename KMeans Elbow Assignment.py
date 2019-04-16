from sklearn import datasets
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import numpy as np

df = datasets.load_iris()

distortions = []
K = range(1,10)
for k in K:
    model = KMeans(n_clusters=k).fit(df.data)
    model.fit(df.data)
    distortions.append(sum(np.min(cdist(df.data, model.cluster_centers_, 'euclidean'), axis=1)) / df.data.shape[0])

plt.plot(K, distortions, 'bx-')
plt.xlabel('K')
plt.ylabel('Distortion')
plt.title('Plot of Elbow Method Showing k is about 3')
plt.show()