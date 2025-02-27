import json
import os

from src.models import Category, Product


def read_json(path: str) -> list[dict]:
    """
    Читает JSON-файл и возвращает его содержимое.

    :param path: Путь к JSON-файлу.
    :return: Список словарей с данными.
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list[Category]:
    """
    Создает объекты Category и Product из JSON-данных.

    :param data: Список словарей с данными о категориях и товарах.
    :return: Список объектов Category.
    """
    categories = []
    for category in data:
        products = []
        for product in category.get("products", []):
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
