import pandas as pd

df  = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"])

#print(df.head())
#print(df.columns)
#print(df.index)
#Index          
#|  A  B  C columns
#0  1  2  3
#1  4  5  6
#2  7  8  9

print(df.describe())
print(df['A'].nunique())
print(df.shape)
print(df.info())
print(df.size)