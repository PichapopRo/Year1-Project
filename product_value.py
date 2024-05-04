from enum import Enum
from processing import *


class Component(Enum):
    GPU = ['Vram', 'Price', 'Clock']
    CPU = ['Core', 'Price']
    SSD = ['Size', 'Price']
    HDD = ['Size', 'Price']
    RAM = ['Size', 'Clock', 'Price']
    Motherboard = ['Price']

