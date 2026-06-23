import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ai_job_dataset1.csv")

top_jobs = (
    df.groupby("job_title")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_jobs.plot(kind="bar")

plt.title("Top 10 Highest Paying AI Job Roles")
plt.xlabel("Job Title")
plt.ylabel("Average Salary (USD)")

plt.tight_layout()

plt.savefig("../screenshots/top_paying_jobs.png")

print("Chart created and saved!")