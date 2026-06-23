import pandas as pd

df = pd.read_csv("../data/ai_job_dataset1.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)




