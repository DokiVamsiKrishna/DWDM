import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import squareform,pdist
a=np.random.random_sample(size=5)
b=np.random.random_sample(size=5)
point=['p1','p2','p3','p4','p5']
data=pd.DataFrame({'point':point,'a':np.round(a,2),'b':np.round(b,2)})
data=data.set_index('point')
print(data)
plt.figure(figsize=(8,5))
plt.scatter(data['a'],data['b'],c='r',marker='*')
plt.xlabel("column a")
plt.ylabel("column b")
plt.title("scatter plot of x and y")
for j in data.itertuples():
    plt.annotate(j.Index,(j.a,j.b),fontsize=15)   
dist=pd.DataFrame(squareform(pdist(data[['a','b']]),'eucliedian'),columns=data.index.values,index=data.index.values)
print("proximity matrix")
print(dist)
plt.figure(figsize=(12,5))
plt.title("Dendogram with single linlage")
dend=shc.dendrogram(shc.linkage(data[['a','b']],method='single'),labels=data.index)
