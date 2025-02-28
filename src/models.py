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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый объект Product или обновляет существующий товар."""
        for category in Category.all_categories:
            for product in category.products_list:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product

        new_product = cls(**product_data)
        return new_product

    @property
    def price(self):
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для изменения цены с проверкой корректности."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
            return

        if new_price < self.__price:
            while True:
                user_choice = input("Вы уверены в снижении цены на товар? [y(yes)/n(no)]: ").strip().lower()
                if user_choice == "y":
                    self.__price = new_price
                    break  # Завершаем цикл после подтверждения
                elif user_choice == "n":
                    return  # Отменяем изменение цены
                else:
                    print("Некорректный ввод. Введите 'y' или 'n'.")
        else:
            self.__price = new_price  # Если цена повышается, просто обновляем


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты класса:
    category_count (int): Общее количество категорий.
    product_count (int): Общее количество товаров во всех категориях.
    """

    category_count = 0
    product_count = 0
    all_categories = []

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        """
        Инициализирует объект категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории (по умолчанию пустой).
        """
        self.name = name
        self.description = description
        self.__products = list(products) if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
        Category.all_categories.append(self)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и обновляет общее количество товаров.

        :param product: Объект класса Product, который нужно добавить.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для получения списка товаров в категории.

        :return: Строка с перечнем товаров и их характеристиками.
        """
        if not self.__products:
            return "В этой категории пока нет товаров."
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):  # Геттер для списка товаров (используется в new_product)
        """Возвращает список товаров."""
        return self.__products
