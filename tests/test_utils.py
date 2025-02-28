import pytest

from src.models import Category, Product
from src.utils import create_objects_from_json, read_json


def test_read_json_success(sample_json) -> None:
    """Проверяет корректность чтения JSON-файла."""
    data = read_json(sample_json)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Смартфоны"


def test_read_json_invalid() -> None:
    """Проверка выброса ошибки при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        read_json("non_existent.json")


def test_create_objects_from_json():
    """Проверяет корректность создания объектов Category и Product."""
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {"name": "Samsung Galaxy", "description": "256GB", "price": 100000.0, "quantity": 10},
                {"name": "iPhone 15", "description": "512GB", "price": 200000.0, "quantity": 5},
            ],
        }
    ]
    categories = create_objects_from_json(data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products_list) == 2
    assert isinstance(categories[0].products_list[0], Product)
    assert categories[0].products_list[0].name == "Samsung Galaxy"
    assert categories[0].products_list[0].price == 100000.0
