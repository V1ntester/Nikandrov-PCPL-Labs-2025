"""Domain entities module for task implementation algorithm.

This is module provides domain subject enteties.

Classes:
    Part: Represents a manufacturing part with attributes.
    Manufacturer: Represents a manufacturer with attributes.
    PartsManufacturers: Represents a relationships between parts and manufacturers
""" 

from .part import Part
from .manufacturer import Manufacturer
from .parts_manufacturers import PartsManufacturers

__all__ = ["Part", "Manufacturer", "PartsManufacturers"]
__version__ = "0.1.0"


def get_version():
    return __version__
