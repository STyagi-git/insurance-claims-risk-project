# insurance_data_cleaning.py

import pandas as pd
import os

# Dynamically get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to raw data folder and output folder
raw_data_dir = os.path.join(script_dir, "..", "raw")
raw_data_dir = os.path.normpath(raw_data_dir)

# Load datasets using dynamic paths
claims_file = os.path.join(raw_data_dir, "Insurance_Claims_Data.csv")
customers_file = os.path.join(raw_data_dir, "Insurance_Customers_Data.csv")

# Load the datasets using your actual file paths
claims_data = pd.read_csv(claims_file)
customers_data = pd.read_csv(customers_file)

# Preview the first few rows of each dataset
print("Claims Data Preview:")
print(claims_data.head())

print("\nCustomers Data Preview:")
print(customers_data.head())

# Check for missing values
print("\nMissing values in Claims Data:")
print(claims_data.isnull().sum())

print("\nMissing values in Customers Data:")
print(customers_data.isnull().sum())

# Check data types
print("\nData types in Claims Data:")
print(claims_data.dtypes)

print("\nData types in Customers Data:")
print(customers_data.dtypes)

# Remove any duplicate rows
claims_data = claims_data.drop_duplicates()
customers_data = customers_data.drop_duplicates()

# Standardize column names to lowercase
claims_data.columns = claims_data.columns.str.lower()
customers_data.columns = customers_data.columns.str.lower()

# Merge the datasets on 'customer_id'
merged_data = pd.merge(claims_data, customers_data, on='customer_id', how='inner')

# Preview the merged dataset
print("\nCleaned and Merged Data Preview:")
print(merged_data.head())

# Build paths to processed data folder and output folder
processed_data_dir = os.path.join(script_dir, "..", "processed")
processed_data_dir = os.path.normpath(processed_data_dir)

# Save the cleaned dataset to a new CSV file
merged_file = os.path.join(processed_data_dir, "Cleaned_Merged_Insurance_Data.csv")
merged_data.to_csv(merged_file, index=False)
print("\nCleaned dataset saved as 'Cleaned_Merged_Insurance_Data.csv'")

