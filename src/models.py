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

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.

        :return: Строка в формате "Название продукта, цена руб. Остаток: количество шт."
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Складывает два товара, вычисляя их общую стоимость на складе.

        :param other: Прибавляемый объект класса 'Product'.
        :return: Общая стоимость товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Сложение возможно только между объектами класса 'Product'")

        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
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
    def price(self) -> float:
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
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

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        :return: Строка в формате "Название категории, количество продуктов: остаток шт."
        """
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и обновляет общее количество товаров.

        :param product: Объект класса Product, который нужно добавить.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в категории.

        :return: Строка с перечнем товаров и их характеристиками.
        """
        if not self.__products:
            return "В этой категории пока нет товаров."
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self) -> list:  # Геттер для списка товаров (используется в new_product)
        """Возвращает список товаров."""
        return self.__products


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category: Category) -> None:
        """
        Инициализирует итератор.

        :param category: Объект класса 'Category'.
        """
        self.__products = category.products_list
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает сам объект итератора."""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар из списка."""
        if self.index < len(self.__products):
            product = self.__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
