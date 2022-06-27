from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
doc1="Deep Learning Can Be Hard"
doc2="Deep Learning Can Be Simple"
documents=[doc1,doc2]
count_vectorizer=CountVectorizer()
rep_matrix=count_vectorizer.fit_transform(documents)
print(rep_matrix)
doc_matrix=rep_matrix.todense()
print(doc_matrix)
df=pd.DataFrame(doc_matrix,columns=count_vectorizer.get_feature_names(),index=['doc1','doc2'])
print(df)
print('Similarity Matrix:\n',cosine_similarity(df,df))
