from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления продукта."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict) -> "BaseProduct":
        """Абстрактный метод создания или обновления товара."""
        pass


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с названием и описанием."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления объекта."""
        pass
