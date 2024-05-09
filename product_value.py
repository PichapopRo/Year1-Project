from enum import Enum
from processing import *


class Component(Enum):
    GPU = ['Vram', 'Price', 'Clock', 'TDP']
    CPU = ['Cores', 'Threads', 'Turbo Clock', 'Price', 'TDP']
    SSD = ['Size', 'Price', 'Clock']
    HDD = ['Size', 'Price']
    RAM = ['Size', 'Clock', 'Price']
    Motherboard = ['Price', 'Memory Capacity', 'RAM Slots']

