"""Module for representing manufacturing parts."""

from dataclasses import dataclass, field


@dataclass(order=True)
class Part:
    """Represents a manufacturing part.

    Attributes:
        id: Unique identifier for the part.
        manufacturer_id: identifier for the manufacturer.
        name: Name of the part.
        weight: Weight of the part in grams.
        category: Category of the part.
        production_cost: Production cost in currency units.
    """

    id: int = field(compare=False)
    manufacturer_id: int = field(compare=False)
    name: str = field(compare=False)
    weight: int = field(compare=False)
    category: str = field(compare=False)
    production_cost: int = field(compare=True)

    def __eq__(self, other):
        """Checks equality based on part attributes."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.manufacturer_id == other.manufactorer_id
            and self.name == other.name
            and self.weight == other.weight
            and self.category == other.category
            and self.production_cost == other.production_cost
        )
