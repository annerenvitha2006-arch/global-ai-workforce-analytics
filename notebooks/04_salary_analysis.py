import pandas as pd

df = pd.read_csv("../data/ai_job_dataset1.csv")

salary_by_role = (
    df.groupby("job_title")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("TOP 10 HIGHEST PAYING JOB ROLES")
print(salary_by_role.head(10))