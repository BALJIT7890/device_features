import pandas as pd
import csv

file_path = 'device_features.csv'

# Open the CSV file and create a reader object
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
data = pd.read_csv(file_path)

#Below code has been continued from previous tasks
# c1. Create a chart to visually represent the proportion of RAM types for devices in the current market.
import matplotlib.pyplot as plt
ram_type_counts = loaded_data['ram_type'].value_counts(normalize=True)

# Plotting the pie chart
plt.figure(figsize=(15, 6))
ram_type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Proportion of RAM Types for Devices')
plt.axis('equal')
plt.legend(title='RAM Types', loc='best')
plt.show()

#c2) Create a chart to visually compare the number of devices for each USB connector type

usb_counts = loaded_data['usb_connector'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(15, 6))
usb_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Devices for Each USB Connector Type')
plt.xlabel('USB Connector Type')
plt.ylabel('Number of Devices')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

