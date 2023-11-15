import os
import pandas as pd

# Define the file name of the imported file
file_name = 'surfanalysis.txt'

# Read the text file
with open(file_name, 'r') as file:
    data = file.readlines()

# Extract data from "Number of surface minima" section
minima_data = []
is_minima_section = False
for line in data:
    if "Number of surface minima" in line:
        is_minima_section = True
        continue
    if "Number of surface maxima" in line:
        break
    if is_minima_section and line.strip():
        values = line.split()
        if values[3] != 'kcal/mol':
            try:
                value = float(values[3])
                minima_data.append(value)
            except ValueError:
                pass

# Extract data from "Number of surface maxima" section to the end
maxima_data = []
is_maxima_section = False
for line in data:
    if "Number of surface maxima" in line:
        is_maxima_section = True
        continue
    if is_maxima_section and line.strip():
        values = line.split()
        if values[3] != 'kcal/mol':
            try:
                value = float(values[3])
                maxima_data.append(value)
            except ValueError:
                pass

# Sort the data
sorted_minima_data = sorted(minima_data)
sorted_maxima_data = sorted(maxima_data, reverse=True)

# Create DataFrames for minima and maxima
df_minima = pd.DataFrame([sorted_minima_data], columns=[f"Minima_{i+1}" for i in range(len(sorted_minima_data))])
df_maxima = pd.DataFrame([sorted_maxima_data], columns=[f"Maxima_{i+1}" for i in range(len(sorted_maxima_data))])

# Add file name column
df_minima.insert(0, 'File Name', os.path.splitext(file_name)[0])
df_maxima.insert(0, 'File Name', os.path.splitext(file_name)[0])

# Create Excel writer and export DataFrames to Excel
with pd.ExcelWriter('output.xlsx') as writer:
    df_minima.to_excel(writer, sheet_name='Minima', index=False)
    df_maxima.to_excel(writer, sheet_name='Maxima', index=False)
