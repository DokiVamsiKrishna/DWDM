import pandas as pd
import numpy as np
import copy 
from sklearn.preprocessing import LabelEncoder
df_flights=pd.read_csv("flights.csv")
print(df_flights.head())
print('\n\n\n\n')
print(df_flights.info())
print('\n\n\n\n')

#Filter the categorical data
cat_df_flights=df_flights.select_dtypes(include=['object']).copy()
print(cat_df_flights)
print('\n\n\n\n')

#checking the Null values
print('checking the Null values')
print(cat_df_flights.isnull().values.sum())
print('\n\n\n\n')

#check the column wise Null values
print('check the column wise Null values')
print(cat_df_flights.isnull().sum())
print('\n\n\n\n')

#check the frequency distribution of the values in a cloumn
print('check the frequency distribution of the values in a cloumn')
print(cat_df_flights['UniqueCarrier'].value_counts())
print('\n\n\n\n')

print('Total Number of categories in FlightNum column:',cat_df_flights['UniqueCarrier'].value_counts().count())
print('\n\n\n\n')

#Label Encoding
cat_df_flights_lc=cat_df_flights.copy()
cat_df_flights_lc['UniqueCarrier']=cat_df_flights_lc['UniqueCarrier'].astype('category')

print(cat_df_flights_lc.dtypes)
print('\n\n\n\n')

cat_df_flights_lc['UniqueCarrier']=cat_df_flights_lc['UniqueCarrier'].cat.codes

print(cat_df_flights_lc)
print('\n\n\n\n')

#Label Encoding using sklearn
lb_make=LabelEncoder()
cat_sklearn=cat_df_flights.copy()
cat_sklearn['UniqueCarrier']=lb_make.fit_transform(cat_df_flights['UniqueCarrier'])
print(cat_sklearn)
print('\n\n\n\n')

#one_Hot Encoding sklearn 
cat_onehot=cat_df_flights.copy()
cat_onehot=pd.get_dummies(cat_onehot,columns=['UniqueCarrier'],prefix=['UniqueCarrier'])
print(cat_onehot)

