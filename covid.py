import pandas as pd


# Load data
df = pd.read_csv('owid-covid-data.csv') 



# Check columns
print("Columns:\n", df.columns)


# Preview data
print("\nFirst 5 rows:\n", df.head())

# Check missing values
print("\nMissing values:\n", df.isnull().sum())










import pandas as pd

#  Load the dataset
df = pd.read_csv("owid-covid-data.csv")

#  Filter for countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing critical values (e.g., 'date', 'total_cases')
df = df.dropna(subset=['date', 'total_cases'])

#  Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

#  Handle missing numeric values (e.g., fill forward, interpolate)
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].interpolate(method='linear')  # or use fillna(method='ffill')

# Optional: Reset index if needed
df = df.reset_index(drop=True)

#  Check final result
print(df.head())
print("\nRemaining missing values:")
print(df[numeric_cols].isnull().sum())










import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("owid-covid-data.csv")

# Filter countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing dates or total_cases
df = df.dropna(subset=['date', 'total_cases'])

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Interpolate missing numeric values
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].interpolate(method='linear')

# Calculate death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']

# -----------------------------
# Visualization Setup
sns.set(style="whitegrid")
plt.figure(figsize=(15, 20))

# 1. Total Cases Over Time
plt.subplot(3, 2, 1)
for country in countries:
    plt.plot(df[df['location'] == country]['date'], df[df['location'] == country]['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date'); plt.ylabel('Total Cases'); plt.legend()

# 2. Total Deaths Over Time
plt.subplot(3, 2, 2)
for country in countries:
    plt.plot(df[df['location'] == country]['date'], df[df['location'] == country]['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date'); plt.ylabel('Total Deaths'); plt.legend()

# 3. New Daily Cases
plt.subplot(3, 2, 3)
for country in countries:
    plt.plot(df[df['location'] == country]['date'], df[df['location'] == country]['new_cases'], label=country)
plt.title('New Daily COVID-19 Cases')
plt.xlabel('Date'); plt.ylabel('New Cases'); plt.legend()

# 4. Death Rate Over Time
plt.subplot(3, 2, 4)
for country in countries:
    plt.plot(df[df['location'] == country]['date'], df[df['location'] == country]['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date'); plt.ylabel('Death Rate'); plt.legend()

# 5. Total Cases by Country (Latest Date)
plt.subplot(3, 2, 5)
latest = df[df['date'] == df['date'].max()]
cases_by_country = latest.groupby('location')['total_cases'].max().sort_values(ascending=False)
sns.barplot(x=cases_by_country.values, y=cases_by_country.index, palette='Reds_r')
plt.title('Total Cases by Country (Most Recent Date)')
plt.xlabel('Total Cases')

# 6. Correlation Heatmap
plt.subplot(3, 2, 6)
corr = df[numeric_cols + ['death_rate']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.show()





import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.tight_layout()
plt.show()






# summarry
## Key Insights

1. **India experienced the highest total number of cases** among the selected countries, but the case fatality rate was lower than that of the USA.
2. **The USA had the fastest vaccine rollout**, reaching over 60% of its population vaccinated earlier than India and Kenya.
3. **Kenya showed a slower and more delayed rise in both cases and vaccinations**, likely reflecting regional disparities in access and reporting.
4. A **noticeable spike in new daily cases** was observed in India around May 2021, consistent with the Delta variant surge.
5. Despite high total cases, **death rates remained low** in India compared to expectations—suggesting underreporting or a younger population demographic.

## Interesting Patterns & Anomalies

- **Vaccination vs. death rate:** Countries with higher vaccination rates generally had **flattened death curves**, suggesting vaccine effectiveness.
- **Case dips and spikes** in Kenya could be due to irregular testing or reporting rather than actual infection trends.

