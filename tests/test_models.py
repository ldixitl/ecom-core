import pytest

from src.exceptions import ZeroQuantityError
from src.models import Category, CategoryIterator, LawnGrass, Product


def test_product_creation(first_product) -> None:
    """Проверяет корректность создания объекта Product."""
    assert first_product.name == "Samsung Galaxy"
    assert first_product.description == "256GB, Серый цвет"
    assert first_product.price == 100000.0
    assert first_product.quantity == 10


def test_product_str(first_product) -> None:
    """Проверяет строковое представление товара."""
    assert str(first_product) == "Samsung Galaxy, 100000.0 руб. Остаток: 10 шт."


def test_product_add(first_product, second_product) -> None:
    """Проверяет корректность сложения двух товаров, вычисляя их общую стоимость на складе."""
    assert first_product + second_product == 2000000


def test_product_add_type_check(first_product) -> None:
    """Проверяет, что нельзя сложить объекты разного класса."""

    class NotAProduct:
        pass

    not_a_product = NotAProduct()

    with pytest.raises(TypeError, match="Сложение возможно только между объектами класса 'Product'"):
        first_product + not_a_product


def test_product_add_different_types(first_product) -> None:
    """Проверяет, что нельзя сложить товары разных типов."""
    lawn_grass = LawnGrass("Газонная трава", "Быстрорастущая", 500.0, 20, "Россия", "14 дней", "Зеленый")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        first_product + lawn_grass


def test_smartphone_creation(smartphone) -> None:
    """Проверяет корректность создания объекта Smartphone."""
    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "Флагманский смартфон Apple"
    assert smartphone.price == 120000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 9500.0
    assert smartphone.model == "14 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "черный"


def test_smartphone_str(smartphone) -> None:
    """Проверяет строковое представление смартфона."""
    assert str(smartphone) == "iPhone 14 (14 Pro), черный, 256 ГБ, 120000.0 руб. Остаток: 5 шт."


def test_lawn_grass_creation(lawn_grass) -> None:
    """Проверяет корректность создания объекта LawnGrass."""
    assert lawn_grass.name == "GreenLife"
    assert lawn_grass.description == "Быстрорастущая газонная трава"
    assert lawn_grass.price == 1500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Германия"
    assert lawn_grass.germination_period == "10-14 дней"
    assert lawn_grass.color == "зеленый"


def test_lawn_grass_str(lawn_grass) -> None:
    """Проверяет строковое представление газонной травы."""
    assert str(lawn_grass) == "GreenLife, зеленый, Германия, прорастание: 10-14 дней, 1500.0 руб. Остаток: 20 шт."


def test_add_product_type_check(empty_category) -> None:
    """Проверяет, что в категорию нельзя добавить объект, не являющийся Product."""

    class NotAProduct:
        pass

    not_a_product = NotAProduct()

    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников."):
        empty_category.add_product(not_a_product)


def test_category_creation(empty_category) -> None:
    """Проверяет корректность создания объекта Category и обновление счетчика категорий."""
    assert empty_category.name == "Смартфоны"
    assert empty_category.description == "Описание смартфонов"
    assert empty_category.products_list == []


def test_category_str(category_with_products) -> None:
    """Проверяет строковое представление категории, включая подсчет общего количества товаров."""
    assert str(category_with_products) == "Смартфоны, количество продуктов: 15 шт."


def test_category_add_product(empty_category, first_product) -> None:
    """Проверяет добавление продукта в категорию и обновление счетчика товаров."""
    initial_product_count = Category.product_count

    empty_category.add_product(first_product)

    assert len(empty_category.products_list) == 1
    assert empty_category.products_list[0] == first_product
    assert Category.product_count == initial_product_count + 1


def test_category_add_product_invalid(empty_category) -> None:
    """Проверяет, что нельзя добавить объект, не являющийся Product."""

    class NotAProduct:
        pass

    with pytest.raises(TypeError):
        empty_category.add_product(NotAProduct())


def test_category_initial_products(category_with_products) -> None:
    """Проверяет корректность установки товаров при создании категории."""
    assert len(category_with_products.products_list) == 2


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
    product.price = -10
    message = capsys.readouterr().out.strip().split("\n")

    assert message[1] == "Цена не должна быть нулевая или отрицательная."
    assert message[2] == "Цена не должна быть нулевая или отрицательная."


def test_new_product_creation() -> None:
    """Проверяет создание нового товара через new_product."""
    product_data = {"name": "MacBook Pro", "description": "16 дюймов, M2 Pro", "price": 300000.0, "quantity": 3}

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "MacBook Pro"
    assert product.description == "16 дюймов, M2 Pro"
    assert product.price == 300000.0
    assert product.quantity == 3


def test_new_product_creation_exception() -> None:
    """Проверяет выброс ошибки при создании нового товара через new_product с нулевым количеством."""
    product_data = {"name": "MacBook Pro", "description": "16 дюймов, M2 Pro", "price": 300000.0, "quantity": 0}

    with pytest.raises(
        ZeroQuantityError, match="Товар 'MacBook Pro' не может иметь нулевое количество при создании или заказе."
    ):
        Product.new_product(product_data)


def test_product_zero_quantity():
    """Проверяет, что нельзя создать товар с нулевым количеством."""
    with pytest.raises(
        ZeroQuantityError, match="Товар 'Тестовый товар' не может иметь нулевое количество при создании или заказе."
    ):
        Product("Тестовый товар", "Описание", 1000.0, 0)


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


def test_category_average_price(category_with_products, first_product, second_product, empty_category) -> None:
    """Проверяет расчет среднего ценника товаров в категории."""
    expected_avg_price = (first_product.price + second_product.price) / 2
    assert category_with_products.avg_price() == expected_avg_price

    assert empty_category.avg_price() == 0


def test_category_iterator(category_with_products, product_list) -> None:
    """Проверяет корректность работы итератора по товарам категории."""
    iterator = CategoryIterator(category_with_products)
    assert iterator.index == 0

    # Проверяем, что итератор проходит по всем товарам в правильном порядке
    for product in product_list:
        assert next(iterator) == product

    # Проверяем, что итератор выбрасывает StopIteration после последнего элемента
    with pytest.raises(StopIteration):
        next(iterator)
