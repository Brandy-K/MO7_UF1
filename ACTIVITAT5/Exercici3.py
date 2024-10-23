import pandas as pd
import matplotlib.pyplot as plt

# Read the file
filepath = "archive/test.csv"
df = pd.read_csv(filepath)
# Select the Ids
id_mobils = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
def mostrarclockspeed():

    df_filtered = df[df['id'].isin(id_mobils)][['id', 'clock_speed']]  # filter the data

    print(df_filtered)

def mostrarmegapixels():

    df_filtered = df[df['id'].isin(id_mobils)][['id', 'px_height']]


    print(df_filtered)

def mostrabateria():
    df_filtered = df[df['id'].isin(id_mobils)][['id', 'battery_power']]
    print(df_filtered)
# call the functions
mostrarclockspeed()
mostrarmegapixels()
mostrabateria()

# plot the graph
def plots(data, title, xlabel, ylabel, column_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the bar plot
    ax.bar(data['id'], data[column_name], color='skyblue')

    # Set titles and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Main function
def main():
    filepath = "archive/test.csv"
    df = pd.read_csv(filepath)

    id_mobils = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

    # Plot Battery Power
    df_battery = df[df['id'].isin(id_mobils)][['id', 'battery_power']]
    title_battery = "Battery Power of Selected Mobile IDs"
    xlabel_battery = "Mobile ID"
    ylabel_battery = "Battery Power (mAh)"
    plots(df_battery, title_battery, xlabel_battery, ylabel_battery, 'battery_power')

    # Plot Clock Speed
    df_clock_speed = df[df['id'].isin(id_mobils)][['id', 'clock_speed']]
    title_clock_speed = "Clock Speed of Selected Mobile IDs"
    xlabel_clock_speed = "Mobile ID"
    ylabel_clock_speed = "Clock Speed (GHz)"
    plots(df_clock_speed, title_clock_speed, xlabel_clock_speed, ylabel_clock_speed, 'clock_speed')

    # Plot megapixels
    df_megapixels = df[df['id'].isin(id_mobils)][['id', 'px_height']]
    title_megapixels = "Megapixels of Selected Mobile IDs"
    xlabel_megapixels = "Mobile ID"
    ylabel_megapixels = "megapixels"
    plots(df_megapixels, title_megapixels, xlabel_megapixels, ylabel_megapixels, 'px_height')


# call the main
if __name__ == "__main__":
    main()

