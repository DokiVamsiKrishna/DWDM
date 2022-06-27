from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_text
import numpy as np
import graphviz
#load iris dataset
iris=load_iris()
#divide dependent and independent data
x,y=iris.data,iris.target
#split the data into training and test data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
#create object for decision tree
clf = tree.DecisionTreeClassifier()
#fit the data
clf=clf.fit(x_train,y_train)
print("predicted value\t true value")
for (i,j) in zip(clf.predict(x_test),y_test):
	print(i,"\t\t",j)
#predict the test data using model
y_pred=clf.predict(x_test)
print("accuracy: ",metrics.accuracy_score(y_test,y_pred))
r = export_text(clf, feature_names=iris['feature_names'])
print(r)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")
dot_data = tree.export_graphviz(clf, out_file=None,feature_names=iris.feature_names,
class_names=iris.target_names,
filled=True, rounded=True,
special_characters=True)
graph = graphviz.Source(dot_data)
print('decisiontree classification model :')
graph


