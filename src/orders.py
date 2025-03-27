from src.abstract import BaseEntity
from src.models import Product


class Order(BaseEntity):
    """Класс, представляющий заказ на покупку одного товара."""

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Создает заказ на товар.

        :param product: Экземпляр товара.
        :param quantity: Количество единиц товара в заказе.
        """
        if quantity > product.quantity:
            raise ValueError(f"Недостаточно товара {product.name} на складе. В наличии: {product.quantity} шт.")

        super().__init__(product.name, product.description)

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

        # Уменьшаем количество товара на складе.
        product.quantity -= quantity

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"Заказ: {self.quantity} x {self.product.name} = {self.total_price} руб."
