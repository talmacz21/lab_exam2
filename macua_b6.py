import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  
df = pd.read_csv(file_path)

# Creating the 'HRID' column by concatenating 'Location', 'Site', and 'Replicate', separated by dashes
# Also, replacing any commas with dashes in these fields
df['HRID'] = df['Location'].str.replace(',', '-') + '-' + df['Site'].str.replace(',', '-') + '-' + df['Replicate'].astype(str)

# Save the updated dataframe to a new CSV file
output_file_path_with_hrid = 'Macua_B6_answer.csv'  # Replace with your desired output file name
df.to_csv(output_file_path_with_hrid, index=False)
