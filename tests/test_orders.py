from src.orders import Order


def test_order_creation(first_product) -> None:
    """Проверяет корректность создания заказа."""
    order = Order(first_product, 3)
    assert order.product == first_product
    assert order.quantity == 3
    assert order.total_price == 300000.0  # 100000 * 3


def test_order_exceeds_stock(capsys, first_product) -> None:
    """Проверяет, что нельзя заказать больше товара, чем есть на складе."""
    Order(first_product, 20)
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Ошибка: Недостаточно товара Samsung Galaxy на складе. В наличии: 10 шт."
    )
    assert message.out.strip().split("\n")[-1] == "Обработка заказа завершена."


def test_order_reduces_stock(first_product) -> None:
    """Проверяет, что после заказа количество товара уменьшается."""
    initial_stock = first_product.quantity
    Order(first_product, 2)
    assert first_product.quantity == initial_stock - 2


def test_order_str(first_product) -> None:
    """Проверяет строковое представление заказа."""
    order = Order(first_product, 1)
    assert str(order) == "Заказ: 1 x Samsung Galaxy = 100000.0 руб."


def test_order_zero_quantity(capsys, first_product) -> None:
    """Проверяет, что нельзя создать заказ с нулевым количеством товара."""
    Order(first_product, 0)
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Ошибка: Товар 'Samsung Galaxy' не может иметь нулевое количество при создании или заказе."
    )
    assert message.out.strip().split("\n")[-1] == "Обработка заказа завершена."
