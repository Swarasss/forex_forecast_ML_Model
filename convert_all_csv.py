import csv
import os

DATA_DIR = "edgar_data"

# Loop through all files in the directory
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".tsv"):
        input_file = os.path.join(DATA_DIR, filename)
        output_file = os.path.join(DATA_DIR, filename.replace(".tsv", ".csv"))

        with open(input_file, mode="r", encoding="utf-8") as tsv_file, \
             open(output_file, mode="w", encoding="utf-8", newline="") as csv_file:
            
            reader = csv.reader(tsv_file, delimiter="\t")
            writer = csv.writer(csv_file)

            for row in reader:
                writer.writerow(row)

        print(f"Converted {filename} to {os.path.basename(output_file)}")
