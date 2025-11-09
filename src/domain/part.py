"""Module for representing manufacturing parts."""


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

    def __init__(
        self,
        part_id: int,
        manufacturer_id: int,
        name: str,
        weight: int,
        category: str,
        production_cost: int,
    ):
        self.id = part_id
        self.manufacturer_id = manufacturer_id
        self.name = name
        self.weight = weight
        self.category = category
        self.production_cost = production_cost

    def __eq__(self, other):
        """Checks equality based on part attributes."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.manufactorer_id == other.manufactorer_id
            and self.name == other.name
            and self.weight == other.weight
            and self.category == other.category
            and self.production_cost == other.production_cost
        )

    def __hash__(self):
        """Returns hash based on part attributes."""
        return hash(
            (
                self.manufactorer_id,
                self.name,
                self.weight,
                self.category,
                self.production_cost,
            )
        )

    def __lt__(self, other):
        """Compares parts based on production cost."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.production_cost < other.production_cost
