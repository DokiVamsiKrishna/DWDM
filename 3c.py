import numpy as np
from scipy.spatial.distance import jaccard
a=np.array([1,0,0,1,1,1])
b=np.array([0,0,1,1,1,1])
d=jaccard(b,a)
print("Distance:",d)
