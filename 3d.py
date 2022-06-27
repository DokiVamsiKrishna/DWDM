from sklearn.metrics.pairwise import euclidean_distances
X=[[0,1],[1,1]]
# distance between rows of X
print(euclidean_distances(X,X))
# get distance to origin
print(euclidean_distances(X,[[0,0]]))
