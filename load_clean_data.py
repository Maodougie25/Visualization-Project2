import pandas as pd

# Load the dataset
try:
    data = pd.read_csv("Final-50-stocks.csv")  # Ensure this is the correct file name
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The file 'Final-50-stocks.csv' was not found.")
    exit()

# Display dataset info
print("\nDataset Info:")
print(data.info())

# Display the first few rows
print("\nFirst Few Rows:")
print(data.head())