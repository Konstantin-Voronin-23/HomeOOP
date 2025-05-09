from src.Product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_init(self):
        """Проверка корректности инициализации продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_attributes_types(self):
        """Проверка типов атрибутов продукта"""
        product = Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)
