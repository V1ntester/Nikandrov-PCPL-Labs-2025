"""Domain entities module for task implementation algorithm.

This is module provides domain subject enteties.

Classes:
    Part: Represents a manufacturing part with attributes.
    Manufacturer: Represents a manufacturer with attributes.
"""

from .part import Part
from .manufacturer import Manufacturer

__all__ = ["Part", "Manufacturer"]
__version__ = "0.1.0"


def get_version():
    return __version__
