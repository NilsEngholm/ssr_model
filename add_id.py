import pandas as pd

file1 = r'C:\Users\Nilse\ssr_model\merged_file.csv'
file2 = r'C:\Users\Nilse\ssr_model\top_skaters_women.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

df2['ID'] = df2['ID'].astype(int)

df1['Full Name'] = df1['Family Name'] + ',' + df1['Given Name']
df2['Full Name'] = df2['Family Name'] + ',' + df2['Given Name']

df1 = pd.merge(df1, df2[['ID', 'Full Name']], on='Full Name', how='left', suffixes=('', '_new'))

df1['ID'] = df1['ID'].combine_first(df1['ID_new'])

df1 = df1.drop(columns=['Full Name', 'ID_new'])

output_file = r'C:\Users\Nilse\ssr_model\merged_file_final.csv'
df1.to_csv(output_file, index=False)

print("The merged file has been updated successfully.")