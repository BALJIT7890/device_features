# device_features
import pandas as pd
import csv

file_path = 'device_features.csv'

# Open the CSV file and create a reader object
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
data = pd.read_csv(file_path)

print("Summary of the dataset:")
print(data.info())

data.shape

print(data.isnull().sum())

# a1) Retrieve the model name, manufacturer, weight, price, and price currency for the device(s) based on the oem_id.

def load_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def retrieve_device_info_by_oem_id(data, specified_oem_id):
    device_info = []
    for device in data:
        if device['oem_id'] == specified_oem_id:
            device_info.append({
                'model': device['model'],
                'manufacturer': device['manufacturer'],
                'weight': device['weight_gram'],
                'price': device['price'],
                'price_currency': device['price_currency']
            })
    return device_info

file_path = input("Enter the path to the CSV file: ")
loaded_data = load_data(file_path)

specified_oem_id = input("Enter the oem_id to retrieve device info: ")

result = retrieve_device_info_by_oem_id(loaded_data, specified_oem_id)
if result:
    print("Device(s) information based on oem_id:", specified_oem_id)
    for device in result:
        print(f"Model Name: {device['model']}")
        print(f"Manufacturer: {device['manufacturer']}")
        print(f"Weight: {device['weight']}")
        print(f"Price: {device['price']} {device['price_currency']}")
        print("-" * 20)
else:
    print("No device found for the provided oem_id.")

#a2) Retrieve the brand, model name, RAM capacity, market regions, and the date when the information was added for the device(s) associated with a specified code name**

def retrieve_device_info_by_code_name(data, specified_code_name):
    device_info = []
    for device in data:
        if device['codename'] == specified_code_name:
            device_info.append({
                'brand': device['brand'],
                'model': device['model'],
                'ram_capacity': device['ram_capacity'],
                'market_region': device['market_regions'],
                'info_added_date': device['info_added_date']
            })
    return device_info

loaded_data = load_data(file_path)

specified_code_name = input("Enter the code name to retrieve device info: ")

result = retrieve_device_info_by_code_name(loaded_data, specified_code_name)
if result:
    print(f"Device(s) information based on Code name '{specified_code_name}':")
    for device in result:
        print(f"Brand: {device['brand']}")
        print(f"Model name: {device['model']}")
        print(f"Ram capapcity: {device['ram_capacity']}")
        print(f"Market region: {device['market_region']}")
        print(f"Date of info added: {device['info_added_date']}")
        print("-" * 20)
else:
    print("No device found for the provided RAM capacity.")

#a3) Retrieve the oem_id, release date, announcement date, dimensions, and device category of the device(s) based on a specified RAM capacity

def retrieve_device_info_by_ram_capacity(data, specified_ram_capacity):
    device_info = []
    for device in data:
        if device['ram_capacity'] == specified_ram_capacity:
            device_info.append({
                'oem_id': device['oem_id'],
                'released_date': device['released_date'],
                'announced_date': device['announced_date'],
                'dimensions': device['dimensions'],
                'device_category': device['device_category']
            })
    return device_info

loaded_data = load_data(file_path)

specified_ram_capacity = input("Enter the RAM capacity to retrieve device info: ")

result = retrieve_device_info_by_ram_capacity(loaded_data, specified_ram_capacity)
if result:
    print(f"Device(s) information based on RAM capacity '{specified_ram_capacity}':")
    for device in result:
        print(f"oem_id: {device['oem_id']}")
        print(f"Release Date: {device['released_date']}")
        print(f"Announcement Date: {device['announced_date']}")
        print(f"Dimensions: {device['dimensions']}")
        print(f"Device Category: {device['device_category']}")
        print("-" * 20)
else:
    print("No device found for the provided RAM capacity.")

# a4) Retrieve hardware designer, battery capacity, price, RAM capacity and general features associated with a specified Brand

def retrieve_device_info_by_brand(data, specified_brand):
    device_info = []
    for device in data:
        if device['brand'] == specified_brand:
            device_info.append({
                'hardware_designer': device['hardware_designer'],
                'battery_capacity': device['battery_capacity'],
                'price': device['price'],
                'ram_capacity': device['ram_capacity'],
                'general_extras': device['general_extras']
            })
    return device_info


loaded_data = load_data(file_path)

specified_brand = input("Enter the device brand or name to retrieve device info: ")  # Provide the desired identifier

result = retrieve_device_info_by_brand(loaded_data, specified_brand)
if result:
    print(f"Device information associated with '{specified_brand}':")
    for device in result:
        print(f"Hardware Designer: {device['hardware_designer']}")
        print(f"Battery capacity: {device['battery_capacity']}")
        print(f"Price: {device['price']}")
        print(f"Ram capacity: {device['ram_capacity']}")
        print(f"General feature: {device['general_extras']}")
        print("-" * 20)  # Separator between devices
else:
    print("No device found for the provided identifier.")
