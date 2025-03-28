from src.models import LawnGrass, Product, Smartphone


def test_logging_mixin(capsys) -> None:
    """Тест логирования создания объектов"""
    product = Product("Samsung Galaxy", "256GB, Серый цвет", 100000.0, 10)
    smartphone = Smartphone("iPhone 14", "Флагманский смартфон Apple", 120000.0, 5, 9500.0, "14 Pro", 256, "черный")
    lawn_grass = LawnGrass(
        "GreenLife", "Быстрорастущая газонная трава", 1500.0, 20, "Германия", "10-14 дней", "зеленый"
    )

    assert product is not None
    assert smartphone is not None
    assert lawn_grass is not None

    message = capsys.readouterr().out.strip().split("\n")
    assert message[0] == "Product(Samsung Galaxy, 256GB, Серый цвет, 100000.0, 10)"
    assert message[1] == "Smartphone(iPhone 14, Флагманский смартфон Apple, 120000.0, 5)"
    assert message[2] == "LawnGrass(GreenLife, Быстрорастущая газонная трава, 1500.0, 20)"
