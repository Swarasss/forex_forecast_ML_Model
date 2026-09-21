import os
import zipfile

# Use the current working directory
data_dir = os.getcwd()  # This gets the current directory you're in (i.e., 'edgar_data')

# ZIP filename
zip_filename = 'edgar_filings_csv_files.zip'

# Path to save the zip file
zip_file_path = os.path.join(data_dir, zip_filename)

# Create a Zip file to store the CSV files
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Loop through the directory and find all .csv files
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                # Add the file to the zip archive
                zipf.write(file_path, os.path.relpath(file_path, data_dir))

print(f"All CSV files from {data_dir} have been zipped into {zip_filename}")
