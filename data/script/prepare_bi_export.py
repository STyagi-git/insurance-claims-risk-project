import pandas as pd
import os

# Dynamically get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to processed data folder and output folder
processed_data_dir = os.path.join(script_dir, "..", "processed")
processed_data_dir = os.path.normpath(processed_data_dir)

# Load the fraud-checked data
file_path = os.path.join(processed_data_dir, "Risk_Scored_Insurance_Data_FraudChecked.csv")
data = pd.read_csv(file_path)

# Select only relevant columns for Tableau
powerbi_ready = data[[
    'customer_id',
    'claim_id',
    'claim_amount',
    'claim_frequency',
    'high_claim_flag',
    'fraud_risk_flag'
]]

# Build paths to final data folder and output folder
final_data_dir = os.path.join(script_dir, "..", "final")
final_data_dir = os.path.normpath(final_data_dir)

# Save to a clean export file
output_path = os.path.join(final_data_dir, "PowerBI_Insurance_Claims_Data.csv")
powerbi_ready.to_csv(output_path, index=False)

print(" Power BI export created. File saved to:")
print(output_path)
