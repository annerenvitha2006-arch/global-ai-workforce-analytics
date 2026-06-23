import pandas as pd

df = pd.read_csv("../data/ai_job_dataset1.csv")

print("TOTAL JOBS:")
print(len(df))

print("\nAVERAGE SALARY (USD):")
print(round(df["salary_usd"].mean(), 2))

print("\nNUMBER OF COUNTRIES:")
print(df["company_location"].nunique())

print("\nREMOTE JOBS (%):")
print(round((df["remote_ratio"] == 100).mean() * 100, 2))