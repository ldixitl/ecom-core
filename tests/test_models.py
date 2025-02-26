from src.models import Category, Product


def test_product_creation() -> None:
    """Проверяет корректность создания объекта Product."""
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)

    assert product.name == "Samsung Galaxy"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 100000.0
    assert product.quantity == 10


def test_category_creation() -> None:
    """Проверяет корректность создания объекта Category и обновление счетчика категорий."""
    initial_category_count = Category.category_count
    category = Category("Смартфоны", "Описание смартфонов")

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert category.products == []
    assert Category.category_count == initial_category_count + 1


def test_category_add_product() -> None:
    """Проверяет добавление продукта в категорию и обновление счетчика товаров."""
    initial_product_count = Category.product_count
    category = Category("Смартфоны", "Описание смартфонов")
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)

    category.add_product(product)

    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == initial_product_count + 1


def test_category_initial_products() -> None:
    """Проверяет корректность установки товаров при создании категории."""
    initial_product_count = Category.product_count
    products = [
        Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10),
        Product("iPhone 15", "512GB, Gray space", 200000.0, 5),
    ]
    category = Category("Смартфоны", "Описание смартфонов", products)

    assert len(category.products) == 2
    assert Category.product_count == initial_product_count + 2
