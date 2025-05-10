import unittest
from io import StringIO
from unittest.mock import patch

from src.Product import Product


class TestProductOne:
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


class TestProductTwo:
    def test_new_product_creates_new_instance(self):
        """Тест создания нового продукта, когда такого продукта еще нет в списке"""
        product_data = {
            'name': 'Телефон',
            'description': 'Смартфон',
            'price': 50000.0,
            'quantity': 10
        }
        product = Product.new_product(product_data, [])
        assert product.name == 'Телефон'
        assert product.description == 'Смартфон'
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_new_product_updates_existing_product(self):
        """Тест обновления существующего продукта"""
        existing_product = Product('Телефон', 'Смартфон', 50000.0, 5)
        product_data = {
            'name': 'Телефон',
            'description': 'Новый смартфон',
            'price': 55000.0,
            'quantity': 3
        }
        updated_product = Product.new_product(product_data, [existing_product])
        assert updated_product is existing_product
        assert updated_product.quantity == 8  # 5 + 3
        assert updated_product.price == 55000.0  # новая цена выше

    def test_new_product_keeps_higher_price(self):
        """Тест что сохраняется более высокая цена при обновлении продукта"""
        existing_product = Product('Телефон', 'Смартфон', 50000.0, 5)
        product_data = {
            'name': 'Телефон',
            'description': 'Новый смартфон',
            'price': 45000.0,
            'quantity': 3
        }
        updated_product = Product.new_product(product_data, [existing_product])
        assert updated_product.price == 50000.0  # старая цена остается
        assert updated_product.quantity == 8  # количество обновилось

    def test_price_getter(self):
        """Тест геттера цены"""
        product = Product('Телефон', 'Смартфон', 50000.0, 5)
        assert product.price == 50000.0

    def test_price_setter_valid_price(self):
        """Тест сеттера цены с валидным значением"""
        product = Product('Телефон', 'Смартфон', 50000.0, 5)
        product.price = 60000.0
        assert product.price == 60000.0

    def test_price_setter_invalid_price(self):
        """Тест сеттера цены с невалидным значением (<= 0)"""
        product = Product('Телефон', 'Смартфон', 50000.0, 5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            product.price = -100.0
            assert product.price == 50000.0  # цена не изменилась
            assert "Цена не должна быть нулевая или отрицательная" in fake_out.getvalue()

    @patch('builtins.input', return_value='n')
    def test_price_setter_lower_price_rejected(self, mock_input):
        """Тест отмены понижения цены"""
        product = Product('Телефон', 'Смартфон', 50000.0, 5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            product.price = 40000.0
            assert product.price == 50000.0  # цена не изменилась
            assert "Изменение цены отменено" in fake_out.getvalue()

    @patch('builtins.input', return_value='y')
    def test_price_setter_lower_price_accepted(self, mock_input):
        """Тест подтверждения понижения цены"""
        product = Product('Телефон', 'Смартфон', 50000.0, 5)
        product.price = 40000.0
        assert product.price == 40000.0  # цена изменилась

    def test_new_product_with_empty_list(self):
        """Тест создания нового продукта при пустом списке"""
        product_data = {
            'name': 'Телефон',
            'description': 'Смартфон',
            'price': 50000.0,
            'quantity': 10
        }
        product = Product.new_product(product_data)
        assert isinstance(product, Product)
        assert product.name == 'Телефон'
        assert product.description == 'Смартфон'
        assert product.price == 50000.0
        assert product.quantity == 10


class TestProductMethods(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        self.product2 = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)
        self.product3 = Product("Планшет", "Графический планшет", 30000.0, 8)

    def test_product_str(self):
        """Тест метода __str__ класса Product"""
        self.assertEqual(
            str(self.product1),
            "Телефон, 50000.0 руб. Остаток: 10 шт."
        )
        self.assertEqual(
            str(self.product2),
            "Ноутбук, 100000.0 руб. Остаток: 5 шт."
        )

    def test_product_add(self):
        """Тест метода __add__ класса Product"""
        # Проверка корректного сложения
        self.assertEqual(self.product1 + self.product2, 50000.0 * 10 + 100000.0 * 5)
        self.assertEqual(self.product2 + self.product3, 100000.0 * 5 + 30000.0 * 8)

        # Проверка сложения с неправильным типом
        with self.assertRaises(TypeError):
            self.product1 + "не продукт"

        with self.assertRaises(TypeError):
            self.product1 + 123
