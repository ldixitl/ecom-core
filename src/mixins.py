class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self) -> None:
        """Выводит информацию о создании объекта."""
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
