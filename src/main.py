"""Main application module"""

from src.domain import Part, Manufacturer, PartsManufacturers


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

PartsManufacturers = [
    PartsManufacturers(0, 0),
    PartsManufacturers(1, 1),
    PartsManufacturers(2, 1),
    PartsManufacturers(3, 2),
    PartsManufacturers(4, 3),
    PartsManufacturers(0, 2),
]


def first_task(original_one_to_many):
    """Return manufacturers starting with 'G' and their parts."""
    print("\nЗадание Г1:")

    one_to_many = sorted(original_one_to_many, key=lambda x: x["manufacturer_id"])

    manufacturer_parts = []

    for part in one_to_many:
        manufacturer_name = part["manufacturer_name"]
        if manufacturer_name[0] == "G":
            manufacturer_parts.append(part)

    return manufacturer_parts


def print_first_task_result(manufacturer_parts):
    """Print manufacturers starting with 'G' and their parts."""
    previous_manufacturer_name = ""

    for part in manufacturer_parts:
        manufacturer_name = part["manufacturer_name"]
        if not manufacturer_name or manufacturer_name[0] != "G":
            continue
        if manufacturer_name != previous_manufacturer_name:
            previous_manufacturer_name = manufacturer_name
            print(f"\nПроизводитель {manufacturer_name}:")

        part_name = part["name"]
        print(part_name)


def second_task(original_one_to_many):
    """Return the most expensive part for each manufacturer."""

    one_to_many = sorted(
        original_one_to_many, key=lambda x: x["production_cost"], reverse=True
    )

    most_expensive_parts = []
    previous_manufacturers_ids = set()

    for part in one_to_many:
        manufacturer_id = part["manufacturer_id"]
        if manufacturer_id not in previous_manufacturers_ids:
            previous_manufacturers_ids.add(manufacturer_id)

            manufacturer_name = part["manufacturer_name"]
            name = part["name"]
            production_cost = part["production_cost"]

            most_expensive_parts.append(
                {
                    "manufacturer_name": manufacturer_name,
                    "name": name,
                    "production_cost": production_cost,
                }
            )

    return most_expensive_parts


def print_second_task_result(most_expensive_parts):
    """Print the most expensive part for each manufacturer."""
    print("\nЗадание Г2:")

    for part in most_expensive_parts:
        print(
            f"Производитель: {part["manufacturer_name"]}; "
            f"Запчасть: {part["name"]}; "
            f"Себестоимость производства: {part["production_cost"]}"
        )


def third_task(original_many_to_many):
    """Return manufacturers and their parts sorted by production capacity."""
    many_to_many = sorted(
        original_many_to_many,
        key=lambda x: x["manufacturer_production_capacity"],
        reverse=True,
    )

    manufacturers = dict()

    for manufacturer_part in many_to_many:
        if manufacturer_part["manufacturer_id"] not in manufacturers:
            manufacturers[manufacturer_part["manufacturer_id"]] = {
                "manufacturer_name": manufacturer_part["manufacturer_name"],
                "manufacturer_production_capacity": manufacturer_part[
                    "manufacturer_production_capacity"
                ],
                "parts": [],
            }

        manufacturers[manufacturer_part["manufacturer_id"]]["parts"].append(
            manufacturer_part["part_name"]
        )

    return manufacturers


def print_third_task_result(manufacturers):
    print("\nЗадание Г3:")

    previous_manufacturer_name = ""

    for manufacturer in manufacturers.values():
        manufacturer_name = manufacturer["manufacturer_name"]

        if manufacturer_name != previous_manufacturer_name:
            previous_manufacturer_name = manufacturer["manufacturer_name"]
            manufacturer_production_capacity = manufacturer[
                "manufacturer_production_capacity"
            ]

            print(
                f"\nПроизводитель {manufacturer_name} (Производственная "
                f"мощность {manufacturer_production_capacity}):"
            )

        for part in manufacturer["parts"]:
            print(part)


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

    print_first_task_result(first_task(one_to_many))
    print_second_task_result(second_task(one_to_many))

    many_to_many_temp = [
        {
            "manufacturer_id": part_manufacturer.manufacturer_id,
            "part_id": part_manufacturer.part_id,
            "manufacturer_name": manufacturer.name,
            "manufacturer_production_capacity": manufacturer.production_capacity,
        }
        for manufacturer in manufacturers
        for part_manufacturer in PartsManufacturers
        if manufacturer.id == part_manufacturer.manufacturer_id
    ]

    many_to_many = [
        {
            "manufacturer_id": manufacturer_part["manufacturer_id"],
            "manufacturer_name": manufacturer_part["manufacturer_name"],
            "manufacturer_production_capacity": manufacturer_part[
                "manufacturer_production_capacity"
            ],
            "part_name": part.name,
        }
        for manufacturer_part in many_to_many_temp
        for part in parts
        if part.id == manufacturer_part["part_id"]
    ]

    print_third_task_result(third_task(many_to_many))


if __name__ == "__main__":
    main()
