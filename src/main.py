"""Main application module"""

from domain import Part, Manufacturer


class PartsManufacturers:
    """Represents a many-to-many relationship between parts and manufacturers.

    Attributes:
        part_id: The unique identifier of the part.
        manufacturer_id: The unique identifier of the manufacturer.
    """

    def __init__(self, part_id: int, manufacturer_id: int):
        self.part_id = part_id
        self.manufacturer_id = manufacturer_id


parts = [
    Part(0, 0, "Поршень двигателя V8", 450, "Двигатель", 2500),
    Part(1, 1, "Турбокомпрессор ТКР-7", 3200, "Система наддува", 18500),
    Part(2, 1, "Катализатор", 2800, "Выхлопная система", 12200),
    Part(3, 2, "Рычаг подвески верхний", 1850, "Подвеска", 4700),
    Part(4, 3, "Фара светодиодная би-ксенон", 950, "Освещение", 8900),
]

manufacturers = [
    Manufacturer(
        0,
        "Bosch Автокомпоненты",
        "Автомобильные компоненты",
        "Системы впрыска",
        500000,
        "+7 (495) 123-45-67",
        "bosch@example.com",
    ),
    Manufacturer(
        1,
        "Garrett Motion",
        "Автомобильные системы",
        "Турбонаддув",
        200000,
        "+7 (495) 234-56-78",
        "garrett@example.com",
    ),
    Manufacturer(
        2,
        "ZF Friedrichshafen",
        "Автомобильные системы",
        "Подвеска и трансмиссия",
        300000,
        "+7 (495) 456-78-90",
        "zf@example.com",
    ),
    Manufacturer(
        3,
        "HELLA Russia",
        "Автомобильная электроника",
        "Освещение",
        350000,
        "+7 (495) 567-89-01",
        "hella@example.com",
    ),
]

parts_manufacturers = [
    PartsManufacturers(0, 0),
    PartsManufacturers(1, 1),
    PartsManufacturers(2, 1),
    PartsManufacturers(3, 2),
    PartsManufacturers(4, 3),
    PartsManufacturers(0, 2),
]


def first_task(original_one_to_many):
    """Print manufacturers starting with 'G' and their parts."""
    print("\nЗадание Г1:")

    one_to_many = sorted(original_one_to_many, key=lambda x: x["manufacturer_id"])
    previous_manufacturer_name = ""

    for part in one_to_many:
        manufacturer_name = part["manufacturer_name"]
        if not manufacturer_name or manufacturer_name[0] != "G":
            continue
        if manufacturer_name != previous_manufacturer_name:
            previous_manufacturer_name = manufacturer_name
            print(f"\nПроизводитель {manufacturer_name}:")

        part_name = part["name"]
        print(part_name)


def second_task(original_one_to_many):
    """Print the most expensive part for each manufacturer."""
    print("\nЗадание Г2:")

    one_to_many = sorted(
        original_one_to_many, key=lambda x: x["production_cost"], reverse=True
    )
    previous_manufacturers_ids = set()

    for part in one_to_many:
        manufacturer_id = part["manufacturer_id"]
        if manufacturer_id not in previous_manufacturers_ids:
            previous_manufacturers_ids.add(manufacturer_id)

            manufacturer_name = part["manufacturer_name"]
            name = part["name"]
            production_cost = part["production_cost"]

            print(
                f"Производитель: {manufacturer_name}; "
                f"Запчасть: {name}; "
                f"Себестоимость производства: {production_cost}"
            )


def third_task(original_many_to_many):
    """Print manufacturers and their parts sorted by production capacity."""
    print("\nЗадание Г3:")

    many_to_many = sorted(
        original_many_to_many,
        key=lambda x: x["manufacturer_production_capacity"],
        reverse=True,
    )
    previous_manufacturer_name = ""

    for part_manufacturer in many_to_many:
        manufacturer_name = part_manufacturer["manufacturer_name"]
        if manufacturer_name != previous_manufacturer_name:
            previous_manufacturer_name = part_manufacturer["manufacturer_name"]
            manufacturer_production_capacity = part_manufacturer[
                "manufacturer_production_capacity"
            ]

            print(
                f"\nПроизводитель {manufacturer_name} (Производственная "
                f"мощность {manufacturer_production_capacity}):"
            )

        print(part_manufacturer["part_name"])


def main():
    """Main function."""

    one_to_many = [
        {
            "name": part.name,
            "production_cost": part.production_cost,
            "manufacturer_name": manufacturer.name,
            "manufacturer_id": manufacturer.id,
        }
        for manufacturer in manufacturers
        for part in parts
        if part.manufacturer_id == manufacturer.id
    ]

    first_task(one_to_many)
    second_task(one_to_many)

    many_to_many_temp = [
        {
            "manufacturer_name": manufacturer.name,
            "manufacturer_production_capacity": manufacturer.production_capacity,
            "manufacturer_id": part_manufacturer.manufacturer_id,
            "part_id": part_manufacturer.part_id,
        }
        for manufacturer in manufacturers
        for part_manufacturer in parts_manufacturers
        if manufacturer.id == part_manufacturer.manufacturer_id
    ]

    many_to_many = [
        {
            "manufacturer_name": part_manufacturer["manufacturer_name"],
            "manufacturer_production_capacity": part_manufacturer[
                "manufacturer_production_capacity"
            ],
            "part_name": part.name,
        }
        for part_manufacturer in many_to_many_temp
        for part in parts
        if part.id == part_manufacturer["part_id"]
    ]

    third_task(many_to_many)


if __name__ == "__main__":
    main()
