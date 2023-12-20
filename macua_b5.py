import pandas as pd

# Load the CSV file
file_path = 'table1.csv'  
df = pd.read_csv(file_path)

# Calculating the average count for the species 'Pomacentrus adelus'
average_count_pomacentrus_adelus = df[df['Scientific Name'] == 'Pomacentrus adelus']['Count'].mean()
print(average_count_pomacentrus_adelus)