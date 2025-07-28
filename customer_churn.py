import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("telco_churn.csv")

# Show missing values
print("Missing values:\n", df.isnull().sum())

# Convert TotalCharges to numeric (in case it's an object)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Drop any rows with missing values
df = df.dropna()

# Show first few rows
print(df.head())

# Churn Rate
churn_rate = df['Churn'].value_counts(normalize=True).rename("proportion")
print("\nChurn Rate:\n", churn_rate)

# Churn by Contract Type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title('Churn by Contract Type')
plt.xlabel('Contract Type')
plt.ylabel('Number of Customers')
plt.xticks(rotation=10)
plt.tight_layout()
plt.show()

# Churn by Senior Citizen
senior_churn = df.groupby(['SeniorCitizen', 'Churn']).size().unstack()
senior_churn_pct = senior_churn.div(senior_churn.sum(axis=1), axis=0)

print("\nChurn by SeniorCitizen (raw count):\n", senior_churn)
print("\nChurn by SeniorCitizen (%):\n", senior_churn_pct)

# Plot Churn by Senior Citizen
senior_churn_pct.plot(kind='bar', stacked=True, figsize=(6,4), colormap='Set2')
plt.title("Churn Rate by Senior Citizen")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Proportion")
plt.legend(title='Churn')
plt.tight_layout()
plt.show()

# Average tenure, charges by churn
print("\nAverage values grouped by Churn:")
print(df.groupby("Churn")[["Tenure", "MonthlyCharges", "TotalCharges"]].mean())

# Optional: Save cleaned file for Power BI
df.to_csv("cleaned_churn_data.csv", index=False)
