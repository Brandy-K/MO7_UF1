#  la quantitat de casos total per mes per país
import pandas as pd
import matplotlib.pyplot as plt
# Read the file
filepath = "df_covid19_countries.csv"
df = pd.read_csv(filepath)

# Convert date from object to datetime
df['date'] = pd.to_datetime(df['date'])

# Select 10 unique countries
ten_paisos = df['location'].unique()[:10]

# Filter the data for the top 10 countries
df_filtered = df[df['location'].isin(ten_paisos)][['location', 'total_cases', 'date']]

# Convert 'date' to month-period format
df_filtered['month'] = df_filtered['date'].dt.to_period('M')

# Select the first 4 months
first_4_months = df_filtered['month'].unique()[:4]

# Filter the data for the first 4 months
df_filtered = df_filtered[df_filtered['month'].isin(first_4_months)]

# Group the data by country and month, summing the total cases
df_grouped = df_filtered.groupby(['location', 'month'])['total_cases'].sum().reset_index()

# Function to print the total cases per country per month


def print_cases_per_month(df_grouped):
    for month in first_4_months:
        print(f"\nMes: {month}")
        month_data = df_grouped[df_grouped['month'] == month]
        for _, row in month_data.iterrows():
            print(f"Pais: {row['location']}, Total Cases: {row['total_cases']}")
# Call the function to print the results
print_cases_per_month(df_grouped)


def plot_cases_per_month(df_grouped):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot each country's data
    for pais in ten_paisos:
        country_data = df_grouped[df_grouped['location'] == pais]
        ax.plot(country_data['month'].astype(str), country_data['total_cases'], marker='o', label=pais)

    ax.set_title('Total Cases per Month for 10 Countries')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Cases')
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Call the plotting function
plot_cases_per_month(df_grouped)
