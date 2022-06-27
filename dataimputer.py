import pandas as pd
df=pd.read_csv('stdmarks.csv')
print('ORIGINAL DATA')
print(df)
#replacing the missing values with mean vaues in the column
df['Marks3']=df['Marks3'].fillna(df['Marks3'].mean())
print('REPLACING MARKS WITH MEAN VALUES')
print(df)
#replacing the missing values with frequently used name 
df['Name']=df['Name'].fillna(df['Name'].value_counts().index[0])
print('REPLACING NAMES WITH MOST FREQUENTLY USED NAMES')
print(df)
