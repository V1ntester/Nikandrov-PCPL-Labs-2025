"""Unit tests for the main application module.

This module provides tests for first_task, second_task, and third_task
functions, using pytest fixtures for sample data of parts and manufacturers.
"""

from src.main import first_task, second_task, third_task


def test_first_task_only(one_to_many):
    result = first_task(one_to_many)

    assert len(result) == 3
    assert all(item["manufacturer_name"].startswith("G") for item in result)


def test_second_task(one_to_many):
    result = second_task(one_to_many)

    manufacturers = {
        item["manufacturer_name"]: item["production_cost"] for item in result
    }

    assert manufacturers["GKN Automotive"] == 14300
    assert manufacturers["Denso Corporation"] == 6200
    assert manufacturers["KYB Europe"] == 8800
    assert manufacturers["Girlock Systems"] == 7800


def test_third_task_sorting_and_grouping(many_to_many):
    result = third_task(many_to_many)

    manufacturers = list(result.values())

    assert manufacturers[0]["manufacturer_name"] == "Denso Corporation"
    assert manufacturers[0]["manufacturer_production_capacity"] == 510000

    assert "Полуось привода" in manufacturers[1]["parts"]
