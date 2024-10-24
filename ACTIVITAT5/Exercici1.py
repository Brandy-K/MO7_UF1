import pandas as pd
import matplotlib.pyplot as plt

# Read the file
filepath = "df_covid19_countries.csv"
df = pd.read_csv(filepath)

# Convert date from object to datetime
df['date'] = pd.to_datetime(df['date'])

# Select 10 unique countries
ten_paisos = df['location'].unique()[:10]


# Function to get total cases per month
def totalcasespermonth():
    # Filter the data for the top 10 countries
    df_filtered = df[df['location'].isin(ten_paisos)][['location', 'total_cases', 'date']]

    # Convert date to month format
    df_filtered['month'] = df_filtered['date'].dt.to_period('M')

    # Select the first 4 months
    first_4_months = df_filtered['month'].unique()[:4]

    # Filter the data for the first 4 months
    df_filtered = df_filtered[df_filtered['month'].isin(first_4_months)]

    return df_filtered, first_4_months


# Function to get total deaths per month
def totalDeaths():
    df_filtered = df[df['location'].isin(ten_paisos)][['location', 'total_deaths', 'date']]

    # Convert 'date' to month-period format
    df_filtered['month'] = df_filtered['date'].dt.to_period('M')

    # Select the first 4 months
    first_4_months = df_filtered['month'].unique()[:4]

    # Filter the data for the first 4 months
    df_filtered = df_filtered[df_filtered['month'].isin(first_4_months)]

    return df_filtered, first_4_months


# Function to get reproduction rate per month
def reproduction_rate():
    df_filtered = df[df['location'].isin(ten_paisos)][['location', 'reproduction_rate', 'date']]

    # Convert 'date' to month-period format
    df_filtered['month'] = df_filtered['date'].dt.to_period('M')

    # Select the first 4 months
    first_4_months = df_filtered['month'].unique()[:4]

    # Filter the data for the first 4 months
    df_filtered = df_filtered[df_filtered['month'].isin(first_4_months)]

    return df_filtered, first_4_months


# Function to plot total cases, deaths, or reproduction rate per month for each country
def plots(df_filtered, first_4_months, title, xlabel, ylabel, column_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # group the data for proper plotting
    df_grouped = df_filtered.groupby(['month', 'location'])[column_name].sum().reset_index()

    # Plot each country's data
    for pais in ten_paisos:
        country_data = df_grouped[df_grouped['location'] == pais]
        ax.plot(country_data['month'].astype(str), country_data[column_name], marker='o', label=pais)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main function to run the code
def main():
    # Get filtered data for total cases
    df_filtered_cases, first_4_months_cases = totalcasespermonth()

    # Plot the total cases per month
    title_cases = 'Total Cases per Month for 10 Countries'
    xlabel_cases = 'Month'
    ylabel_cases = 'Total Cases'
    plots(df_filtered_cases, first_4_months_cases, title_cases, xlabel_cases, ylabel_cases, 'total_cases')

    # Get filtered data for total deaths
    df_filtered_deaths, first_4_months_deaths = totalDeaths()

    # Plot the total deaths per month
    title_deaths = 'Total Deaths per Month for 10 Countries'
    xlabel_deaths = 'Month'
    ylabel_deaths = 'Total Deaths'
    plots(df_filtered_deaths, first_4_months_deaths, title_deaths, xlabel_deaths, ylabel_deaths, 'total_deaths')

    # Get filtered data for reproduction rate
    df_filtered_reproduction, first_4_months_reproduction = reproduction_rate()

    # Plot the reproduction rate per month
    title_reproduction = 'Reproduction Rate per Month for 10 Countries'
    xlabel_reproduction = 'Month'
    ylabel_reproduction = 'Reproduction Rate'
    plots(df_filtered_reproduction, first_4_months_reproduction, title_reproduction, xlabel_reproduction,
          ylabel_reproduction, 'reproduction_rate')


if __name__ == "__main__":
    main()
