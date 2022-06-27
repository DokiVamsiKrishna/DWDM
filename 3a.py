from scipy.stats import pearsonr
x=[-2,-1,0,1,2]
y=[4,1,3,2,0]
corr,_=pearsonr(x,y)
print('pearson correlation:',corr)
