import pandas as pd
import os

# Dynamically get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to processed data folder and output folder
processed_data_dir = os.path.join(script_dir, "..", "processed")
processed_data_dir = os.path.normpath(processed_data_dir)

# Load your risk-scored dataset
risk_scored_file_path = os.path.join(processed_data_dir, "Risk_Scored_Insurance_Data.csv")
data = pd.read_csv(risk_scored_file_path)

# Create multiple fake high-claim records for the same customer to simulate fraud
fraud_records = pd.DataFrame({
    'customer_id': ['FAKE_CUST_999'] * 5,
    'policy_id': ['FAKE_POLICY_999'] * 5,
    'claim_amount': [100000] * 5,  # Extremely high claims
    'policy_premium': [500] * 5,
    'risk_score': [0.9] * 5,
    'processing_days': [1] * 5,
    'claim_to_premium_ratio': [200] * 5,
    'is_high_risk': [1] * 5,
    'processing_efficiency': [100000] * 5,
    'claim_id': ['CL_FAKE_001', 'CL_FAKE_002', 'CL_FAKE_003', 'CL_FAKE_004', 'CL_FAKE_005']
})

# Append these fake fraud records to your dataset
data = pd.concat([data, fraud_records], ignore_index=True)

# Save the updated dataset for re-scoring
output_path = os.path.join(processed_data_dir, "Risk_Scored_Insurance_Data_with_FakeFraud.csv")
data.to_csv(output_path, index=False)

print("✅ Fake fraudulent claims added for validation. File saved to:")
print(output_path)