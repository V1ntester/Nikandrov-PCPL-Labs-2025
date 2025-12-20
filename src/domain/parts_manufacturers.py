"""Module for representing relationships."""

from dataclasses import dataclass


@dataclass
class PartsManufacturers:
    """Represents a many-to-many relationship between parts and manufacturers.

    Attributes:
        part_id (int): The unique identifier of the part.
        manufacturer_id (int): The unique identifier of the manufacturer.
    """

    part_id: int
    manufacturer_id: int
