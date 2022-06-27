import pandas as pd
from apyori import apriori
df=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
l=[]
for i in range(0,7501):
	l.append([str(df.values[i,j]) for j in range(0,20)])
association_rules=apriori(l,min_support=0.0045,min_confidence=0.2,min_lift=3,min_length=2)
association_result=list(association_rules)
for i in range(0,len(association_result)):
	print(association_result[i][0])
print("-------------------------------------")
for  item in association_result:
	pair=item[0]
	items=[x for x in pair]
print("Rule: "+items[0]+"->"+items[1])
print("Support : "+str(item[1]))
print("Confidence :" +str(item[2][0][2]))
print("lift: "+str(item[2][0][3]))
print("---------------------------------------------------")
