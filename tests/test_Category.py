from src.Category import Category
from src.Product import Product
import pytest


class TestCategoryOne:
    """Тесты для класса Category"""

    def test_category_init(self):
        """Проверка корректности инициализации категории"""
        category = Category("Электроника", "Техника для дома")

        assert category.name == "Электроника"
        assert category.description == "Техника для дома"
        assert category.products == ""
        assert len(category._Category__products) == 0

    def test_category_with_products(self):
        """Проверка инициализации категории с продуктами"""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)
        ]
        category = Category("Электроника", "Техника для дома", products)

        assert len(category._Category__products) == 2
        assert "Телефон" in category.products
        assert "Ноутбук" in category.products

    def test_total_categories_counter(self):
        """Проверка подсчета количества категорий"""
        assert Category.category_count == 0

        Category("Категория 1", "Описание 1")
        assert Category.category_count == 1

        Category("Категория 2", "Описание 2")
        assert Category.category_count == 2

    def test_product_counter_with_products(self):
        """Проверка подсчета количества продуктов в категории"""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 1),
            Product("Товар 2", "Описание 2", 200.0, 2)
        ]

        category = Category("Категория 1", "Описание 1", products)

        assert len(category._Category__products) == 2

    def test_product_counter_empty_category(self):
        """Проверка, что пустая категория не увеличивает счетчик продуктов"""
        Category("Пустая категория", "Без продуктов")
        assert Category.product_count == 0
        assert Category.category_count == 1


class TestCategoryTwo:
    def test_add_product_valid(self):
        """Тест добавления корректного продукта в категорию"""
        category = Category("Тест", "Тестовая категория")
        product = Product("Тестовый продукт", "Описание", 100, 10)

        category.add_product(product)

        assert len(category._Category__products) == 1
        assert category._Category__products[0] == product

    def test_add_product_invalid_type(self):
        """Тест попытки добавления объекта не типа Product"""
        category = Category("Тест", "Тестовая категория")

        with pytest.raises(TypeError) as excinfo:
            category.add_product("не продукт")

        assert str(excinfo.value) == "Можно добавлять только объекты от класса Product"

    def test_products_property(self):
        """Тест свойства products, возвращающего строковое представление"""
        category = Category("Тест", "Тестовая категория")
        product1 = Product("Продукт 1", "Описание 1", 100, 5)
        product2 = Product("Продукт 2", "Описание 2", 200, 3)

        category.add_product(product1)
        category.add_product(product2)

        expected_output = (
            "Продукт 1, 100 руб. , Остаток: 5 шт.\n"
            "Продукт 2, 200 руб. , Остаток: 3 шт."
        )

        assert category.products == expected_output

    def test_products_property_empty(self):
        """Тест свойства products с пустым списком продуктов"""
        category = Category("Тест", "Тестовая категория")

        assert category.products == ""
