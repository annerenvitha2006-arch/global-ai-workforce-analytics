import pandas as pd

df = pd.read_csv("../data/ai_job_dataset1.csv")

salary_summary = (
    df.groupby("job_title")["salary_usd"]
    .mean()
    .reset_index()
)

salary_summary.to_csv(
    "salary_summary.csv",
    index=False
)

experience_summary = (
    df.groupby("experience_level")["salary_usd"]
    .mean()
    .reset_index()
)

experience_summary.to_csv(
    "experience_summary.csv",
    index=False
)

country_summary = (
    df.groupby("company_location")
    .size()
    .reset_index(name="job_count")
)

country_summary.to_csv(
    "country_summary.csv",
    index=False
)

df.to_csv(
    "cleaned_jobs.csv",
    index=False
)

print("Dashboard files created successfully!")