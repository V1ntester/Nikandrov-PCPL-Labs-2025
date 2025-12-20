"""
Pytest fixtures for testing the main application module.

Provides sample data for one-to-many and many-to-many relationships
between parts and manufacturers, to be used in unit tests.
"""

import pytest
from src.domain import Part, Manufacturer, PartsManufacturers


@pytest.fixture
def parts():
    return [
        Part(0, 0, "Гидравлический усилитель руля", 2000, "Рулевое управление", 9600),
        Part(1, 0, "Полуось привода", 3500, "Привод", 14300),
        Part(2, 1, "Тормозной суппорт передний", 1800, "Тормоза", 7800),
        Part(3, 2, "Радиатор охлаждения", 1200, "Охлаждение", 5400),
        Part(4, 2, "Датчик массового расхода воздуха", 400, "Датчики", 6200),
        Part(5, 3, "Амортизатор задний", 2500, "Подвеска", 8800),
    ]


@pytest.fixture
def manufacturers():
    return [
        Manufacturer(
            0,
            "GKN Automotive",
            "Автомобильные системы",
            "Рулевое управление",
            420000,
            "+7 111 111-11-11",
            "gkn@example.com",
        ),
        Manufacturer(
            1,
            "Girlock Systems",
            "Автомобильные системы",
            "Тормоза",
            180000,
            "+7 222 222-22-22",
            "girlock@example.com",
        ),
        Manufacturer(
            2,
            "Denso Corporation",
            "Автомобильные компоненты",
            "Охлаждение и датчики",
            510000,
            "+7 333 333-33-33",
            "denso@example.com",
        ),
        Manufacturer(
            3,
            "KYB Europe",
            "Автомобильные системы",
            "Подвеска",
            290000,
            "+7 444 444-44-44",
            "kyb@example.com",
        ),
    ]


@pytest.fixture
def parts_manufacturers():
    return [
        PartsManufacturers(0, 0),
        PartsManufacturers(1, 0),
        PartsManufacturers(2, 1),
        PartsManufacturers(3, 2),
        PartsManufacturers(4, 2),
        PartsManufacturers(5, 3),
    ]


@pytest.fixture
def one_to_many(parts, manufacturers):
    return [
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


@pytest.fixture
def many_to_many(parts, manufacturers, parts_manufacturers):
    many_to_many_temp = [
        {
            "manufacturer_id": part_manufacturer.manufacturer_id,
            "part_id": part_manufacturer.part_id,
            "manufacturer_name": manufacturer.name,
            "manufacturer_production_capacity": manufacturer.production_capacity,
        }
        for manufacturer in manufacturers
        for part_manufacturer in parts_manufacturers
        if manufacturer.id == part_manufacturer.manufacturer_id
    ]

    return [
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
