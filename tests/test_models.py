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
    assert category.products_list == []
    assert Category.category_count == initial_category_count + 1


def test_category_add_product() -> None:
    """Проверяет добавление продукта в категорию и обновление счетчика товаров."""
    initial_product_count = Category.product_count
    category = Category("Смартфоны", "Описание смартфонов")
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)

    category.add_product(product)

    assert len(category.products_list) == 1
    assert category.products_list[0] == product
    assert Category.product_count == initial_product_count + 1


def test_category_initial_products() -> None:
    """Проверяет корректность установки товаров при создании категории."""
    initial_product_count = Category.product_count
    products = [
        Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10),
        Product("iPhone 15", "512GB, Gray space", 200000.0, 5),
    ]
    category = Category("Смартфоны", "Описание смартфонов", products)

    assert len(category.products_list) == 2
    assert Category.product_count == initial_product_count + 2


def test_product_price_setter(monkeypatch) -> None:
    """Проверяет работу сеттера price, включая подтверждение снижения цены."""
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)

    # Проверяем повышение цены
    product.price = 110000.0
    assert product.price == 110000.0

    # Проверяем отмену снижения цены
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 90000.0
    assert product.price == 110000.0  # Цена не изменилась

    # Проверяем подтвержденное снижение цены
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 90000.0
    assert product.price == 90000.0  # Цена изменилась


def test_product_price_invalid(capsys) -> None:
    """Проверяет работу сеттера price при некорректной цене"""
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)

    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная."

    product.price = -10
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная."


def test_new_product_creation() -> None:
    """Проверяет создание нового товара через new_product."""
    product_data = {"name": "MacBook Pro", "description": "16 дюймов, M2 Pro", "price": 300000.0, "quantity": 3}

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "MacBook Pro"
    assert product.description == "16 дюймов, M2 Pro"
    assert product.price == 300000.0
    assert product.quantity == 3


def test_new_product_update_existing() -> None:
    """Проверяет обновление количества и цены существующего товара в new_product."""
    category = Category("Ноутбуки", "Описание ноутбуков")
    existing_product = Product("MacBook Pro", "16 дюймов, M2 Pro", 300000.0, 3)
    category.add_product(existing_product)

    updated_data = {"name": "MacBook Pro", "description": "16 дюймов, M2 Pro", "price": 320000.0, "quantity": 2}

    updated_product = Product.new_product(updated_data)

    assert updated_product is existing_product
    assert updated_product.quantity == 5  # Количество обновилось
    assert updated_product.price == 320000.0  # Цена обновилась на максимальную
