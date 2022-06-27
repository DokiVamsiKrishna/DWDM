from sklearn.metrics.pairwise import manhattan_distances
print(manhattan_distances([[3]],[[3]]))
print(manhattan_distances([[3]],[[2]]))
print(manhattan_distances([[2]],[[3]]))
print(manhattan_distances([[1,2],[3,4]],[[1,2],[0,3]]))
import numpy as np
x=np.ones((1,2))
y=np.full((2,2),2.)
manhattan_distances(x,y,sum_over_features=False)
