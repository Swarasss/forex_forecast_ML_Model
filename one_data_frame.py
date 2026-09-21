import pandas as pd
import os

# Directory containing all your CSV files
DATA_DIR = "edgar_data"  # Change to absolute path if needed

# List all CSV files
csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
print(f"Found {len(csv_files)} CSV files in '{DATA_DIR}'")
if not csv_files:
    print("No CSV files found. Please check the directory path.")
    exit()

# Initialize list to hold individual DataFrames
dfs = []

# Process each CSV file
for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    print(f"Reading: {file_path}")
    
    try:
        # Read large files in chunks
        chunk_iter = pd.read_csv(file_path, chunksize=100_000)
        for chunk in chunk_iter:
            chunk['source_file'] = file
            dfs.append(chunk)
    except pd.errors.EmptyDataError:
        print(f" Skipping empty file: {file}")
    except Exception as e:
        print(f" Error reading {file}: {e}")

# Safety check
print(f"Total chunks read: {len(dfs)}")
if not dfs:
    print("No data loaded. Exiting.")
    exit()

# Combine all chunks
combined_df = pd.concat(dfs, ignore_index=True)

# Preview the result
print("✅ Combined shape:", combined_df.shape)
print(combined_df.head())
