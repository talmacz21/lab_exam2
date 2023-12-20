import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  
df = pd.read_csv(file_path)

# Grouping the data by 'Scientific Name' and calculating the average of 'Size Est (cm)'
average_size_per_scientific_name = df.groupby('Scientific Name')['Size Est (cm)'].mean().reset_index()

# Save the result to a new CSV file
output_file_path_avg_size = 'Macua_B4_answer.csv'  
average_size_per_scientific_name.to_csv(output_file_path_avg_size, index=False)