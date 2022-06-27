from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
i=load_iris()
X,Y=i.data,i.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
print("X training set values\tY training set values")
for i in range(0,len(X_train)):
	print(X_train[i],'\t',Y_train[i])
