from enum import Enum


class Component(Enum):
    GPU = ['Vram', 'Price', 'Boost Clock', 'TDP']
    CPU = ['Cores', 'Threads', 'Turbo Clock', 'Price', 'TDP']
    SSD = ['Size', 'Price', 'Clock']
    HDD = ['Size', 'Price']
    RAM = ['Size', 'Clock', 'Price']
    Motherboard = ['Price', 'Memory Capacity', 'RAM Slots']


class DataType(Enum):
    CPU = ['Cores', 'TDP_Numeric']
    RAM = ['Price', 'Size Numeric']
    HDD = ['Price', 'RPM']
    SSD = ['Price', 'Size']
    GPU = ['Price', 'TDP Numeric']
