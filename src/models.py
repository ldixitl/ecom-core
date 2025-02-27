class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует объект товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты класса:
    category_count (int): Общее количество категорий.
    product_count (int): Общее количество товаров во всех категориях.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        """
        Инициализирует объект категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории (по умолчанию пустой).
        """
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и обновляет общее количество товаров.

        :param product: Объект класса Product, который нужно добавить.
        """
        self.products.append(product)
        Category.product_count += 1
