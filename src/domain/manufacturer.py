"""Module for representing manufacturers."""

from dataclasses import dataclass, field


@dataclass(order=True)
class Manufacturer:
    """Represents a manufacturer.

    Attributes:
        id (int): Unique identifier for the manufacturer.
        name (str): Name of the manufacturer.
        industry (str): Industry sector of the manufacturer.
        specialization (str): Specialization area of the manufacturer.
        production_capacity (int): Production capacity in units per time period.
        phone (str): Contact phone number.
        email (str): Contact email address.
    """

    id: int = field(compare=False)
    name: str = field(compare=False)
    industry: str = field(compare=False)
    specialization: str = field(compare=False)
    production_capacity: int = field(compare=True)
    phone: str = field(compare=False)
    email: str = field(compare=False)

    def __eq__(self, other):
        """Checks equality based on manufacturer attributes."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.name == other.name
            and self.industry == other.industry
            and self.specialization == other.specialization
            and self.production_capacity == other.production_capacity
            and self.email == other.email
            and self.phone == other.phone
        )
