import csv
import os

# Define directory
DATA_DIR = "edgar_data"  # Same directory for both TSV and CSV files

# Specify the file to convert (change for other years)
input_file = os.path.join(DATA_DIR, "1993-QTR1.tsv")
output_file = os.path.join(DATA_DIR, "1993-QTR1.csv")  # Same directory, different extension

# Convert TSV to CSV and save in the same directory
with open(input_file, mode="r", encoding="utf-8") as tsv_file, \
     open(output_file, mode="w", encoding="utf-8", newline="") as csv_file:
    
    reader = csv.reader(tsv_file, delimiter="\t")
    writer = csv.writer(csv_file)
    
    for row in reader:
        writer.writerow(row)

print(f"Converted {input_file} to {output_file}")
