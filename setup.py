import os
import pandas as pd
import numpy as np

# Define sample data
np.random.seed(42)
num_entries = 1000  # Number of records

dates = pd.date_range(start="2024-01-01", periods=num_entries, freq='D')
car_types = np.random.choice(['Economy', 'SUV', 'Luxury'], num_entries)
locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Miami'], num_entries)
demand_levels = np.random.uniform(0.4, 1.0, num_entries)
competitor_prices = np.random.uniform(40, 150, num_entries)
temperatures = np.random.uniform(-5, 35, num_entries)
rainfalls = np.random.uniform(0, 20, num_entries)
prices = competitor_prices * (1 + (demand_levels - 0.5))  # Simulate pricing logic

# Create DataFrame
df = pd.DataFrame({
    'date': dates,
    'car_type': car_types,
    'location': locations,
    'demand_level': demand_levels,
    'competitor_price': competitor_prices,
    'temperature': temperatures,
    'rainfall': rainfalls,
    'price': prices
})

# Define the directory and file path
directory = 'data'
file_path = os.path.join(directory, 'car_rental_data.csv')

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the dataframe to the CSV file
df.to_csv(file_path, index=False)
