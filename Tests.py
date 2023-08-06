import pandas as pd
df = pd.read_csv('winereviews.csv')




#print(df[(df['country'] == 'Italy') & (df['variety'] == 'Nebbiolo')])

#print(df[df['country'] == 'Italy'] ['price'].max())

print(df.sort_values(['price'], ascending=False))
