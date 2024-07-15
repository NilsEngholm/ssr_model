import pandas as pd

path = 'C:\\Users\\Nilse\\ssr_model\\merged_file_final.csv'

df = pd.read_csv(path)
df = df.iloc[1:]
df['ID'] = df['ID'].astype(int)
df['Index'] = df['Index'].astype(int)

df.to_csv('Formatted masterlist.csv', index=False)
print(df)