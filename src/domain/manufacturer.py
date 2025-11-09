"""Module for representing manufacturers."""


class Manufacturer:
    """Represents a manufacturer.

    Attributes:
        id: Unique identifier for the manufacturer.
        name: Name of the manufacturer.
        industry: Industry sector of the manufacturer.
        specialization: Specialization area of the manufacturer.
        production_capacity: Production capacity in units per time period.
        phone: Contact phone number.
        email: Contact email address.
    """

    def __init__(
        self,
        manufacturer_id: int,
        name: str,
        industry: str,
        specialization: str,
        production_capacity: int,
        phone: str,
        email: str,
    ):
        self.id = manufacturer_id
        self.name = name
        self.industry = industry
        self.specialization = specialization
        self.production_capacity = production_capacity
        self.phone = phone
        self.email = email

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

    def __hash__(self):
        """Returns hash based on manufacturer attributes."""
        return hash(
            (
                self.name,
                self.industry,
                self.specialization,
                self.production_capacity,
                self.phone,
                self.email,
            )
        )

    def __lt__(self, other):
        """Compares manufacturers based on production capacity."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.production_capacity < other.production_capacity
