import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler
df = pd.read_csv('iris.csv')
x = df.iloc[:, 1:3].values
min_max = MinMaxScaler(feature_range =(0, 1))
min_max1=StandardScaler()
x_after_min_max = min_max.fit_transform(x) 
x_after_min_max1=min_max1.fit_transform(x)
print("Min Max Scaler output is\n", x_after_min_max)
print("Standard Scaler output is\n",x_after_min_max1)
