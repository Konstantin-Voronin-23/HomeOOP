import sys
import unittest
from io import StringIO
from unittest.mock import patch

import pytest

from src.Product import BaseProduct, LawnGrass, Product, Smartphone


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

    def test_add_same_products(self):
        """Сложение товаров одного класса"""
        p1 = Product("Товар 1", "Описание", 100, 2)
        p2 = Product("Товар 2", "Описание", 200, 3)
        assert p1 + p2 == 100 * 2 + 200 * 3

    def test_add_different_product_types(self):
        """Попытка сложить товары разных классов"""
        smartphone = Smartphone("Phone", "Desc", 1000, 1, "High", "X", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 50, 10, "Russia", 14, "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            smartphone + grass

    def test_add_with_non_product(self):
        """Попытка сложить с объектом не класса Product"""
        p = Product("Товар", "Описание", 100, 1)

        with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
            p + "не товар"

    def test_add_smartphones(self):
        """Сложение смартфонов"""
        s1 = Smartphone("S1", "Desc", 1000, 2, "High", "X", 128, "Black")
        s2 = Smartphone("S2", "Desc", 800, 3, "Mid", "Y", 64, "White")
        assert s1 + s2 == 1000 * 2 + 800 * 3

    def test_add_lawn_grass(self):
        """Сложение газонной травы"""
        g1 = LawnGrass("G1", "Desc", 50, 10, "Russia", 14, "Green")
        g2 = LawnGrass("G2", "Desc", 70, 5, "USA", 10, "Blue")
        assert g1 + g2 == 50 * 10 + 70 * 5


class TestSmartphone:
    def test_smartphone_creation(self):
        """Проверка создания объекта смартфона"""
        phone = Smartphone(
            name="iPhone 15",
            description="Флагман Apple",
            price=999,
            quantity=10,
            efficiency="High",
            model="15 Pro",
            memory=256,
            color="Black"
        )

        assert phone.name == "iPhone 15"
        assert phone.price == 999
        assert phone.efficiency == "High"
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert phone.color == "Black"

    def test_smartphone_addition(self):
        """Проверка сложения двух смартфонов"""
        phone1 = Smartphone("Phone1", "Desc", 500, 2, "Mid", "X", 128, "Blue")
        phone2 = Smartphone("Phone2", "Desc", 700, 3, "High", "Y", 256, "Black")

        assert phone1 + phone2 == 500 * 2 + 700 * 3


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        """Проверка создания объекта газонной травы"""
        grass = LawnGrass(
            name="Premium Grass",
            description="Мягкая трава",
            price=50,
            quantity=100,
            country="Russia",
            germination_period=14,
            color="Green"
        )

        assert grass.name == "Premium Grass"
        assert grass.price == 50
        assert grass.country == "Russia"
        assert grass.germination_period == 14
        assert grass.color == "Green"

    def test_lawn_grass_addition(self):
        """Проверка сложения двух упаковок травы"""
        grass1 = LawnGrass("Grass1", "Desc", 40, 20, "USA", 10, "Dark Green")
        grass2 = LawnGrass("Grass2", "Desc", 60, 30, "Germany", 12, "Light Green")

        assert grass1 + grass2 == 40 * 20 + 60 * 30


class TestMixedProducts:
    def test_add_smartphone_and_grass(self):
        """Проверка попытки сложить смартфон и траву"""
        phone = Smartphone("Phone", "Desc", 500, 1, "Mid", "X", 128, "Blue")
        grass = LawnGrass("Grass", "Desc", 50, 10, "Russia", 14, "Green")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            phone + grass


class TestProductClasses(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_base_product_is_abstract(self):
        """Проверяем, что BaseProduct действительно абстрактный"""
        with self.assertRaises(TypeError):
            BaseProduct("Test", "Desc", 100, 5)

    def test_product_creation(self):
        """Тест создания простого продукта"""
        product = Product("Телефон", "Смартфон", 10000, 5)

        self.assertEqual(product.name, "Телефон")
        self.assertEqual(product.description, "Смартфон")
        self.assertEqual(product.price, 10000)
        self.assertEqual(product.quantity, 5)

        output = self.held_output.getvalue()
        self.assertIn("Создан объект класса Product", output)
        self.assertIn("'name': 'Телефон'", output)

    def test_product_str_method(self):
        """Тест метода __str__"""
        product = Product("Телефон", "Смартфон", 10000, 5)
        expected_str = "Телефон, 10000 руб. Остаток: 5 шт."
        self.assertEqual(str(product), expected_str)

    def test_get_total_price(self):
        """Тест метода get_total_price"""
        product = Product("Телефон", "Смартфон", 10000, 3)
        self.assertEqual(product.get_total_price(), 30000)

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        phone = Smartphone("iPhone", "Флагман", 80000, 10, "A15", "13 Pro", 256, "Graphite")

        self.assertEqual(phone.name, "iPhone")
        self.assertEqual(phone.price, 80000)

        self.assertEqual(phone.model, "13 Pro")
        self.assertEqual(phone.memory, 256)

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass("Газон", "Мягкий", 500, 20, "Россия", "14 дней", "Зеленый")

        self.assertEqual(grass.name, "Газон")
        self.assertEqual(grass.quantity, 20)

        self.assertEqual(grass.country, "Россия")
        self.assertEqual(grass.germination_period, "14 дней")

    def test_zero_quantity_raises_error(self):
        """Проверяем, что при quantity=0 возникает ValueError"""
        with self.assertRaises(ValueError):
            Product("Телефон", "Смартфон", 1000.0, 0)

    def test_positive_quantity_works(self):
        """Проверяем, что при quantity>0 объект создается нормально"""
        product = Product("Ноутбук", "Игровой", 2000.0, 3)
        self.assertEqual(product.quantity, 3)
