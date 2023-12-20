import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Transposing the dataframe
transposed_df = df.T

# Resetting the index to make the former column headers become the first column in the transposed dataframe
transposed_df.reset_index(inplace=True)

# Rename the columns appropriately
new_column_names = ['Row Headers'] + list(transposed_df.columns[1:])
transposed_df.columns = new_column_names

# Save the transposed dataframe to a new CSV file
output_file_path_transposed = 'Macua_B7_answer.csv'  # Replace with your desired output file name
transposed_df.to_csv(output_file_path_transposed, index=False)
