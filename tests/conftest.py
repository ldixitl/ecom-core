import json

import pytest

from src.models import Category, Product


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


@pytest.fixture
def first_product() -> Product:
    """Фикстура для первого продукта."""
    return Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)


@pytest.fixture
def second_product() -> Product:
    """Фикстура для второго продукта."""
    return Product("iPhone 15", "512GB, Gray space", 200000.0, 5)


@pytest.fixture
def product_list(first_product, second_product) -> list[Product]:
    """Фикстура для списка продуктов."""
    return [first_product, second_product]


@pytest.fixture
def category_with_products(product_list) -> Category:
    """Фикстура для категории с товарами."""
    return Category("Смартфоны", "Описание смартфонов", product_list)


@pytest.fixture
def empty_category() -> Category:
    """Фикстура для категории без товаров."""
    return Category("Смартфоны", "Описание смартфонов")
