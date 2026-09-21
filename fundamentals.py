
import edgar
import csv

# Define your SEC-compliant user agent
USER_AGENT = "Swara Shinde swara23@vt.edu"

# Set download directory
DOWNLOAD_DIR = "./edgar_data"  # Ensure this directory exists

# Correct function call using 'dest' instead of 'directory'
edgar.download_index(
    DOWNLOAD_DIR,  # Correct positional argument for destination folder
    since_year=1993,
    user_agent=USER_AGENT
)

print(f"Files downloaded in {DOWNLOAD_DIR}")

# Read and inspect the first few lines of a TSV file
file_path = f"{DOWNLOAD_DIR}/1993-QTR1.tsv"  # Change the file name as needed

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")  # TSV uses tab as delimiter
        for i, row in enumerate(reader):
            print(row)  # Print the first few rows to inspect
            if i == 10:  # Limit output to avoid flooding the console
                break
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found. Make sure the download was successful.")

