import pandas as pd
import csv

file_path = 'device_features.csv'

# Open the CSV file and create a reader object
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
data = pd.read_csv(file_path)


#c3) Create separate charts illustrating the monthly average price trends (in GBP) for devices released in each year from 2020 to 2023. Each chart should focus on a specific year.

loaded_data['released_date'] = pd.to_datetime(loaded_data['released_date'])

# Filtering data for each year from 2020 to 2023 and plot the monthly average price trends
for year in range(2020, 2024):
    year_data = loaded_data[loaded_data['released_date'].dt.year == year]
    year_avg_price = year_data.resample('M', on='released_date')['price'].mean()

    plt.figure(figsize=(8, 6))
    plt.plot(year_avg_price.index, year_avg_price.values, marker='o', linestyle='-')
    plt.title(f'Monthly Average Price Trends in {year} (GBP)')
    plt.xlabel('Month')
    plt.ylabel('Average Price (GBP)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# c4. Create a visualisation of your selection to showcase information related to device features that can reveal trends, behaviours, or patterns, ensuring it is distinct from previous requirements.
# Created a visualization to portay number of devices relased by each manufacturer

manufacturer_counts = loaded_data['manufacturer'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(15, 8))
manufacturer_counts.plot(kind='bar', color='green')
plt.title('Number of Devices Released by Each Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Number of Devices Released')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
