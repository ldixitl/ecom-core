class ZeroQuantityError(Exception):
    """Исключение при попытке создать товар или оформить заказ с нулевым количеством."""

    def __init__(self, product_name: str):
        message = f"Товар '{product_name}' не может иметь нулевое количество при создании или заказе."
        super().__init__(message)
