import pandas as pd

df = pd.read_csv("../data/ai_job_dataset1.csv")

print("First 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())