from sklearn.datasets import load_iris
i=load_iris()
X,Y=i.data,i.target
print('independent variable','dependent variable')
for i in range(0,len(X)):
	print(X[i],"\t",Y[i])
