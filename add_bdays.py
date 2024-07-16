import pandas as pd

# Load the CSV files
id_bday_path = r'C:\Users\Nilse\ssr_model\id and bday.csv'
masterlist_path = r'C:\Users\Nilse\ssr_model\Formatted masterlist.csv'

id_bday_df = pd.read_csv(id_bday_path)
masterlist_df = pd.read_csv(masterlist_path)

# Clean the birthday column: replace gender values with NaN
id_bday_df['Birthday'] = id_bday_df['Birthday'].apply(lambda x: x if not x in ['Female', 'Male'] else None)

# Merge the dataframes on the 'ID' column
merged_df = masterlist_df.merge(id_bday_df, on='ID', how='left')

# Save the merged dataframe to a new CSV file
output_path = r'C:\Users\Nilse\ssr_model\masterlist_with_birthday.csv'
merged_df.to_csv(output_path, index=False)

print(f'Merged file saved to {output_path}')
