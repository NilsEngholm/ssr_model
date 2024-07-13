import pandas as pd

# Load the first CSV file
file1 = 'file1.csv'
file2 = 'file2.csv'

df1 = pd.read_csv(file1, header=None)
df2 = pd.read_csv(file2)

# Assigning column names to the first CSV file
df1.columns = ["Rank", "Family Name", "Given Name", "Country", "Time", "Date", "Location", "Event", "Gender", "Year", "Distance"]

# Create a 'Full Name' column in both dataframes for matching
df1['Full Name'] = df1['Family Name'] + ',' + df1['Given Name']
df2['Full Name'] = df2['Family Name'] + ',' + df2['Given Name']

# Merge df1 with df2 on 'Full Name' column
merged_df = pd.merge(df1, df2[['ID', 'Full Name']], on='Full Name', how='left')

# Reorder columns to place 'ID' at the beginning
merged_df = merged_df[['ID'] + df1.columns.tolist()]

# Drop the 'Full Name' column
merged_df = merged_df.drop(columns=['Full Name'])

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)

print("The merged file has been created successfully.")
