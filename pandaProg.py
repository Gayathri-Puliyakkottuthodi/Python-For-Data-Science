import pandas as pd

#storing dictionary into dataframe 
df=pd.DataFrame({'a':[1,2,3],'b':[4,4,5],'c':[4,6,5],'d':[5,6,7],'e':[8,5,3],'f':[3,7,6]})
#print(df.head())
#print(df['a'])

#storing dataframe into .csv file
df.to_csv('file.csv')
df1=pd.read_csv('file.csv')
print(df1.head())

#store dataframe into .xls file
df.to_excel('sample.xls')
df2=pd.read_excel('sample.xls')
#print(df2.head())

#x=df1[ ['z'] ]

print(df1.iloc[2,3])#for exact location index

print(df1.loc[1,'d'])#for labelled index

#to access a part of frame
x=df1.iloc[0:2,0:2]
print(x)

y=df.loc[1:2,'c':'e']
print(y)

#to get unique elements in a column
z=df['b'].unique()
print(z)

#using inequality operators to obtain rows satisfying a condition
print(df['a']>2)

df3=df[df['a']>2]
print(df3)
print(df1.mean())
