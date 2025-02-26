import json

import pytest


@pytest.fixture
def sample_json(tmp_path):
    """Создает временный JSON-файл с тестовыми данными."""
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
    file_path = tmp_path / "test_products.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return file_path
