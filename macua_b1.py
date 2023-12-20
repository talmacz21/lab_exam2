import pandas as pd

# Load the CSV file
file_path = 'table1.csv'
df = pd.read_csv(file_path)

# Filter the dataframe to keep only rows where 'Interval' is '30-0'
filtered_df = df[df['Interval'] == '30-0']

# Save the filtered dataframe to a new CSV file
output_file_path = 'Macua_B1_answer.csv'  
filtered_df.to_csv(output_file_path, index=False)