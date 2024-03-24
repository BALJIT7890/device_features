# Task B
import pandas as pd
import csv

file_path = 'device_features.csv'

# Open the CSV file and create a reader object
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
data = pd.read_csv(file_path)

#b1. Identify the top 5 regions where a specific brand of devices was sold

def load_data(file_path):

    return data

def display_top_regions(data):
    specified_brand = input("Enter the brand name to identify top regions: ")
    brand_data = data[data['brand'] == specified_brand]

    if not brand_data.empty:
        regions = brand_data['market_regions'].str.split(',').explode().str.strip()
        top_regions = regions.value_counts().head(5)
        print(f"Top 5 regions where '{specified_brand}' devices were sold:")
        print(top_regions)
    else:
        print(f"No sales data found for the brand '{specified_brand}'.")

loaded_data = load_data(file_path)

display_top_regions(loaded_data)

#b2. Analyse the average price of devices within a specific brand, all in the same currency.

# Conversion rates from various currencies to INR
exchange_rates = {
    'USD': 0.79,
    'JPY': 0.0055,
    'MXN': 0.046,
    'BRL': 0.16,
    'EUR': 0.87,
    'INR': 0.0094,
    'CNY': 0.11,
    'TWD': 0.025,
    'THB': 0.023,
    'CAD': 0.59,
    'SGD': 0.59,
    'IDR': 0.000051,
    'AED': 0.21,
    'TRY': 0.027,
    'MYR': 0.17,
    'HKD': 0.10,
    'AUD': 0.54,
    'KRW': 0.00061,
    'CHF': 0.92,
    'ARS': 0.00098,
    'KZT': 0.0017,
    'HUF': 0.0023,
    'PLN': 0.20,
    'RUB': 0.0086
}

def convert_to_gbp(row):
    currency = row['price_currency']
    price = row['price']
    if currency == 'GBP':
        return price
    elif currency in exchange_rates:
        return price * exchange_rates[currency]
    else:
        return None
loaded_data['price_GBP'] = loaded_data.apply(convert_to_gbp, axis=1)
print("Updated Dataset with Price in GBP:")
print(loaded_data[['price', 'price_currency', 'price_GBP']])

specified_brand = 'Samsung' # Specifying desired brand name
brand_data = loaded_data[loaded_data['brand'] == specified_brand]


average_price = brand_data['price_GBP'].mean()

print(f"The average price of {specified_brand} is: {average_price:.2f} GBP")

#b3. Analyse the average mass for each manufacturer and display the list of average mass for all manufacturers.

average_mass_by_manufacturer = loaded_data.groupby('manufacturer')['weight_gram'].mean().reset_index()

# Displaying the list of average masses for all manufacturers
print("Average Mass for Each Manufacturer:")
print(average_mass_by_manufacturer)

#b4. Analyse the data to derive meaningful insights based on your unique selection, distinct from the previous requirements.

# Analyze the dataset containing information on manufacturers, hardware designers, and RAM capacities to identify the most prevalent RAM capacity for each hardware designer within different manufacturers.

if isinstance(loaded_data, list):
    loaded_data = pd.DataFrame(loaded_data, columns=['manufacturer', 'hardware_designer', 'ram_capacity'])
grouped_data = loaded_data.groupby(['manufacturer', 'hardware_designer'])['ram_capacity'].apply(lambda x: x.value_counts().idxmax()).reset_index(name='prevalent_ram')

print("Most Prevalent RAM Capacity by Hardware Designer within Each Manufacturer:")
print(grouped_data)


