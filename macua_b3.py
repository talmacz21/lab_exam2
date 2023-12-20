import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  
df = pd.read_csv(file_path)

# Extracting all unique values from the 'Scientific Name' column
unique_scientific_names = df['Scientific Name'].unique()

# Converting the array of unique scientific names to a DataFrame
unique_scientific_names_df = pd.DataFrame(unique_scientific_names, columns=['Scientific Name'])

# Save the DataFrame of unique scientific names to a new CSV file
output_file_path_unique_names = 'Macua_B3_answer.csv'  # Replace with your desired output file name
unique_scientific_names_df.to_csv(output_file_path_unique_names, index=False)