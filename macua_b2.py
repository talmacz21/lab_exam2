import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  
df = pd.read_csv(file_path)

# Fill NaN values in 'Genus' with empty string
df['Genus'].fillna('', inplace=True)

# Filter the dataframe to keep only rows where 'Genus' starts with "St" (case insensitive)
filtered_df_st = df[df['Genus'].str.lower().str.startswith('st')]

# Save the filtered dataframe to a new CSV file
output_file_path_st = 'Macua_B2_answer.csv'  # Replace with your desired output file name
filtered_df_st.to_csv(output_file_path_st, index=False)