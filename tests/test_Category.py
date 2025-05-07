from src.Category import Category
from src.Product import Product


class TestCategory:
    """Тесты для класса Category"""

    def test_category_init(self):
        """Проверка корректности инициализации категории"""
        category = Category("Электроника", "Техника для дома")

        assert category.name == "Электроника"
        assert category.description == "Техника для дома"
        assert category.products == []

    def test_category_with_products(self):
        """Проверка инициализации категории с продуктами"""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)
        ]
        category = Category("Электроника", "Техника для дома", products)

        assert len(category.products) == 2
        assert category.products[0].name == "Телефон"
        assert category.products[1].name == "Ноутбук"

    def test_total_categories_counter(self):
        """Проверка подсчета количества категорий"""
        assert Category.total_categories == 0

        Category("Категория 1", "Описание 1")
        assert Category.total_categories == 1

        Category("Категория 2", "Описание 2")
        assert Category.total_categories == 2

    def test_total_products_counter(self):
        """Проверка подсчета общего количества продуктов"""
        products1 = [
            Product("Товар 1", "Описание 1", 100.0, 1),
            Product("Товар 2", "Описание 2", 200.0, 2)
        ]
        products2 = [
            Product("Товар 3", "Описание 3", 300.0, 3)
        ]

        Category("Категория 1", "Описание 1", products1)
        assert Category.total_products() == 2

        Category("Категория 2", "Описание 2", products2)
        assert Category.total_products() == 3

    def test_empty_category_products_count(self):
        """Проверка что пустая категория не влияет на общий счетчик продуктов"""
        Category("Пустая категория", "Без продуктов")
        assert Category.total_products() == 0
