import pandas as pd
import os

# Directory containing your CSV files — current directory
DATA_DIR = "."

# List all CSV files
csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
print(f" Found {len(csv_files)} CSV files in '{DATA_DIR}'")
if not csv_files:
    print(" No CSV files found. Exiting.")
    exit()

# Load data in chunks (for large files)
dfs = []

for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    print(f" Reading: {file_path}")
    
    try:
        chunk_iter = pd.read_csv(file_path, delimiter='|', chunksize=100_000)
        for chunk in chunk_iter:
            chunk['source_file'] = file
            dfs.append(chunk)
    except pd.errors.EmptyDataError:
        print(f" Skipping empty file: {file}")
    except Exception as e:
        print(f" Error reading {file}: {e}")

# Confirm we have data
print(f" Total data chunks read: {len(dfs)}")
if not dfs:
    print(" No data loaded. Exiting.")
    exit()

# Combine all chunks
combined_df = pd.concat(dfs, ignore_index=True)
print(" Combined DataFrame shape:", combined_df.shape)

# Try to extract a useful date column
date_col_candidates = ['date', 'filing_date', 'report_date', 'accepted_date']

for col in date_col_candidates:
    if col in combined_df.columns:
        print(f" Using '{col}' as date column.")
        combined_df[col] = pd.to_datetime(combined_df[col], errors='coerce')
        combined_df = combined_df.dropna(subset=[col])
        combined_df['year_month'] = combined_df[col].dt.to_period('M').astype(str)
        break
else:
    print(" Could not find a usable date column. No 'year_month' created.")

print(" Preview:")
print(combined_df[['year_month', 'source_file']].head())

monthly_summary = combined_df['year_month'].value_counts().sort_index().reset_index()
monthly_summary.columns = ['year_month', 'filing_count']
print("\n Monthly filing count (first few rows):")
print(monthly_summary.head())


#Wanted a more tight approach, so calculated monthly exchange rates.