

class Category():
    """Класс для названия и описании категорий"""

    total_categories = 0
    all_products = []

    def __init__(self, name: str, description: str, products: list = None):
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.products = products if products else []

        Category.all_products.extend(self.products)
        Category.total_categories += 1

    @classmethod
    def total_products(cls) -> int:
        """Считает общее количество товара во всех категориях"""

        return len(Category.all_products)
