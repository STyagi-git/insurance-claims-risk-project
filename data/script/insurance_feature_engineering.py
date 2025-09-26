import pandas as pd
import os

# Dynamically get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to processed data folder and output folder
processed_data_dir = os.path.join(script_dir, "..", "processed")
processed_data_dir = os.path.normpath(processed_data_dir)

# Load the cleaned dataset
file_path = os.path.join(processed_data_dir, "Cleaned_Merged_Insurance_Data.csv")
data = pd.read_csv(file_path)

# Feature Engineering

# Claim to Premium Ratio
data['claim_to_premium_ratio'] = data['claim_amount'] / data['policy_premium']

# High Risk Flag
data['is_high_risk'] = data['risk_score'].apply(lambda x: 1 if x > 0.7 else 0)

# Processing Efficiency
data['processing_efficiency'] = data['claim_amount'] / data['processing_days']

# Save the updated dataset
output_path = os.path.join(processed_data_dir, "Feature_Engineered_Insurance_Data.csv")
data.to_csv(output_path, index=False)

print(" Feature engineering complete. File saved to:")
print(output_path)
