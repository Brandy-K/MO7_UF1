import pandas as pd
import matplotlib.pyplot as plt
import re

# Read the file once
filepath = "List of world cities by population density.csv"
df = pd.read_csv(filepath)

# Select 10 cities
ten_cities = df['City'].unique()[:10]

# Clean the Population column by removing commas and footnotes like '[1]'
# Simple function to clean the Population column
def clean_population_column(new_string):
    nova_poblacio = new_string.replace(',', '')
    # Remove any non-numeric characters (like [1]
    nova_poblacio = ''.join(char for char in nova_poblacio if char.isdigit() or char == '.')

    # Convert to float
    try:
        return float(nova_poblacio)
    except ValueError:
        return None  # Return None if conversion fails


# Return None if conversion fails

# Apply cleaning to the Population column
df['Population'] = df['Population'].apply(clean_population_column)

def mostrartotalpoblacio():
    df_filtered = df[df['City'].isin(ten_cities)][['City', 'Population']]
    print(df_filtered)

def densitatenkm():
    df_filtered = df[df['City'].isin(ten_cities)][['City', 'Density (/km²)']]
    print(df_filtered)

def densitatenmii():
    df_filtered = df[df['City'].isin(ten_cities)][['City', 'Density (/mi²)']]
    print(df_filtered)

# Display results in the terminal
mostrartotalpoblacio()
densitatenkm()
densitatenmii()

# Function for plotting
def plots(data, title, column_name):
    plt.figure(figsize=(8, 8))
    plt.pie(data[column_name], labels=data['City'], autopct='%1.1f%%', startangle=140)
    plt.legend(data['City'], loc='upper left', bbox_to_anchor=(1, 0.5))
    plt.title(title)

    # Show the plot
    plt.tight_layout()
    plt.show()


def main():
    # Filter the data for the top 10 cities
    df_poblacio = df[df['City'].isin(ten_cities)][['City', 'Population']]

    # Plot the total population by city
    title_poblacio = 'Total Population by City'
    plots(df_poblacio, title_poblacio, 'Population')

    # Plot densitat en km
    df_densitatkm = df[df['City'].isin(ten_cities)][['City', 'Density (/km²)']]
    title_densitatkm = 'Total Density in KM'
    plots(df_densitatkm, title_densitatkm, 'Density (/km²)')

    # Plot densitat en Mii
    df_densitatm = df[df['City'].isin(ten_cities)][['City', 'Density (/mi²)']]
    title_densitatm = 'Total Density in M'
    plots(df_densitatm, title_densitatm, 'Density (/mi²)')

if __name__ == "__main__":
    main()
