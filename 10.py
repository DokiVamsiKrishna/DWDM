import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

centers=[[0.5,2],[-1,-1],[1.5,-1]]
#create data set
X,y=make_blobs(n_samples=100,centers=centers,cluster_std=0.5,random_state=0)
#print(X,y)
X=StandardScaler().fit_transform(X)
print(X,y)
db=DBSCAN(eps=0.4,min_samples=5)
db.fit(X)
labels=db.labels_
n_clusters_=len(set(labels))-(1 if -1 in labels else 0)
print("estimated number of clusters:%d"% n_clusters_)
y_pred=db.fit_predict(X)
print(db.labels_)
plt.figure(figsize=(6,4))
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='Paired')
plt.title('clusters determined by DBSCAN')
plt.show()
