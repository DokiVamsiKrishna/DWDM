import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X=np.array([[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]])
print(X)
plt.scatter(X[:,0],X[:,1])
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
print('\n\nclusters:',kmeans.cluster_centers_)
print('\n\nLabels:\n\n',kmeans.labels_)
#plot the clusters

plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')


print('\n\nclusters:',kmeans.cluster_centers_)
print('\n\nLabels:\n\n',kmeans.labels_)
#plot the clusters

plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
