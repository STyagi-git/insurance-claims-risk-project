# Insurance Claims Risk Project

## Project Overview

This project explores how insurance claims data can be analysed using a complete data workflow in Python.  
It demonstrates **data cleaning, feature engineering, risk scoring, fraud detection**, and preparing clean outputs that can be used by stakeholders to build visual dashboards.

The main aim was to test whether simple rules and engineered features could be used to identify potentially fraudulent claims in a simplified dataset.

---

## Project Goals
- Combine customer and claims data into one dataset
- Create meaningful features that highlight unusual or risky claims
- Add synthetic fraudulent cases for testing
- Apply rule-based scoring to detect suspicious claims
- Provide final outputs for reporting and Power BI dashboards

---

## Data Processing Steps

### 1. Cleaning and Merging Raw Data
- Loaded raw files:  
  - `Insurance_Claims_Data.csv`  
  - `Insurance_Customers_Data.csv`  
- Checked for missing values, duplicates, and inconsistent formats  
- Standardised column names (all lowercase)  
- Merged claims and customer records on `customer_id`  
- **Output:** `Cleaned_Merged_Insurance_Data.csv`

---

### 2. Feature Engineering
- Created new calculated fields:  
  - `claim_to_premium_ratio` → claim size compared to premium paid  
  - `is_high_risk` → flag for customers with risk score > 0.7  
  - `processing_efficiency` → payout per day of processing  
- **Output:** `Feature_Engineered_Insurance_Data.csv`

---

### 3. Adding Claim IDs
- Introduced unique IDs for each claim (`CL101`, `CL102`, …)  
- Helps track claims consistently across datasets  
- **Output:** `Feature_Engineered_Insurance_Data_with_ClaimID.csv`

---

### 4. Injecting Fake Fraud Cases
- Added 5 **synthetic high-risk claims** with extreme values (e.g., very high amounts, 1-day processing)  
- Purpose: test if fraud detection logic correctly identifies them  
- **Output:** `Risk_Scored_Insurance_Data_with_FakeFraud.csv`

---

### 5. Risk Scoring & Fraud Detection
- Applied fraud logic to the dataset, including fake cases:  
  - `claim_frequency` → how often a customer makes claims  
  - `total_claim_amount` → sum of all claims per customer  
  - `high_claim_flag` → marks claims above the 95th percentile  
  - `fraud_risk_flag` → high-value claims + frequent claims  
- **Output:** `Risk_Scored_Insurance_Data_FraudChecked.csv`

---

### 6. Preparing for Power BI
- Selected only the fields needed for dashboarding:  
  `customer_id, claim_id, claim_amount, claim_frequency, high_claim_flag, fraud_risk_flag`  
- Produced two similar BI-ready outputs:  
  - `PowerBI_Insurance_Claims_Data.csv`  
  - `Final_Insurance_Claims_Data.csv`

---

## Stakeholder Recommendations

- Monitor customers with **high claim-to-premium ratios**  
- Investigate customers with **frequent claims**  
- Pay special attention to cases flagged as **high claim value + frequent**  
- Integrate this process into monthly reporting to catch fraud early  

---

## Tech Stack

| Tool     | Purpose |
|----------|-----------------------------------------------|
| Python   | Data cleaning, feature engineering, fraud scoring |
| Pandas   | Data manipulation |
| Power BI | Visualisation and stakeholder dashboards |
| GitHub   | Version control and portfolio hosting |

---

## Project Structure

```
Insurance_Analytics/
├── data/
│   ├── raw/
│   │   ├── Insurance_Claims_Data.csv
│   │   └── Insurance_Customers_Data.csv
│   ├── processed/
│   │   ├── Cleaned_Merged_Insurance_Data.csv
│   │   ├── Feature_Engineered_Insurance_Data.csv
│   │   ├── Feature_Engineered_Insurance_Data_with_ClaimID.csv
│   │   ├── Risk_Scored_Insurance_Data_with_FakeFraud.csv
│   │   ├── Risk_Scored_Insurance_Data_FraudChecked.csv
│   │   ├── PowerBI_Insurance_Claims_Data.csv
│   │   └── Final_Insurance_Claims_Data.csv
├── scripts/
│   ├── insurance_data_cleaning.py
│   ├── insurance_feature_engineering.py
│   ├── add_synthetic_claim_id.py
│   ├── inject_fake_fraud_case.py
│   ├── risk_scoring_fraud_detection.py
│   └── prepare_bi_export.py
└── README.md
```





