import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

gpu_data = pd.read_csv("GPUData.csv").dropna()
CPU_data = pd.read_csv("CPUData.csv").dropna()
mb_data = pd.read_csv("MotherboardData.csv").dropna()
hdd_data = pd.read_csv("HDDData.csv").dropna()
ssd_data = pd.read_csv("SSDData.csv").dropna()
ram_data = pd.read_csv("RAMData.csv").dropna()

gpu_series_mapping = {
    'RTX 3060': 'RTX 30 Series',
    'RTX 3070': 'RTX 30 Series',
    'RTX 3080': 'RTX 30 Series',
    'RTX 3090': 'RTX 30 Series',
    'RTX 3060 Ti': 'RTX 30 Series',
    'GTX 1080': 'GTX 10 Series',
    'GTX 1070': 'GTX 10 Series',
    'GTX 1060': 'GTX 10 Series',
    'GTX 1050 Ti': 'GTX 10 Series',
    'GTX 1050': 'GTX 10 Series',
    'RX 460': 'RX 400 Series',
    'RX 470': 'RX 400 Series',
    'RX 480': 'RX 400 Series',
    'RX 550': 'RX 500 Series',
    'RX 560': 'RX 500 Series',
    'RX 570': 'RX 500 Series',
    'RX 580': 'RX 500 Series',
    'RX 590': 'RX 500 Series',
    'RX 5500 XT': 'RX 5000 Series',
    'RX 5600 XT': 'RX 5000 Series',
    'RX 5700 XT': 'RX 5000 Series',
    'RX 6800': 'RX 6000 Series',
    'RX 6800 XT': 'RX 6000 Series',
    'RX 6900 XT': 'RX 6000 Series',

}


# Function to map GPU series
def map_gpu_series(name):
    for gpu_series, mapped_series in gpu_series_mapping.items():
        if gpu_series in name:
            return mapped_series
    return name


# Create a new column 'series' based on the presence of GPU series in the 'name' column
gpu_data['Series'] = gpu_data['Name'].apply(map_gpu_series)


def convert_to_thb(price_usd):
    exchange_rate_usd_to_thb = 37.02
    casting = float(price_usd.replace("$", "").replace(" USD", ""))
    casted = float(f"{casting * exchange_rate_usd_to_thb:.2f}")
    if casted // 0.5 > 1:
        return math.ceil(casted)
    return math.floor(casted)


def convert_currency_data():
    gpu_data['Price'] = gpu_data['Price'].apply(convert_to_thb)
    CPU_data['Price'] = CPU_data['Price'].apply(convert_to_thb)
    mb_data['Price'] = mb_data['Price'].apply(convert_to_thb)
    hdd_data['Price'] = hdd_data['Price'].apply(convert_to_thb)
    ssd_data['Price'] = ssd_data['Price'].apply(convert_to_thb)
    ram_data['Price'] = ram_data['Price'].apply(convert_to_thb)


def extract_numeric_value(value):
    # Extract numeric value from a string without using re module
    numeric_value = ""
    for char in str(value):
        if char.isdigit():
            numeric_value += char
    if numeric_value:
        return int(numeric_value)
    else:
        return None


convert_currency_data()

