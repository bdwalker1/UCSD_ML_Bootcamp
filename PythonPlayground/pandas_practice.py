import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nicknochnack/Pandasin20Minutes/master/telco_churn.csv')

# print(df.head())
# print(df.tail())

#print(df.describe(include='object'))

#print(df[['State', 'International plan']])

#print(df[(df['International plan']=='No') & (df['Churn']==False)])

#print(df.iloc[22:34,:])

# state = df.copy()
# state.set_index('State', inplace=True)
# print(state.loc['OH'])

df.dropna(inplace=True)
#df.set_index('State', inplace=True)
df.drop('Area code', axis=1, inplace=True)
print(df)
df['newcol'] = df['Total night minutes'] + df['Total intl minutes']
print(df['newcol'])
df['newcol'] = 100
print(df['newcol'])

df['Churn binary'] = df['Churn'].apply(lambda x: 1 if x == True else 0)
print(df[df['Churn binary']==1])

df.to_csv('output.csv')
print(df.to_json())
print(df.to_html())

del df
