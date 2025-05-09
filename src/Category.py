from src.Product import Product


class Category():
    """Класс для названия и описании категорий"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""

        if not isinstance(product, Product):
            raise f"Можно добавлять только объекты от класса Product"

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление товаров"""

        return "\n".join(
            f"{product.name}, {product.price} руб. , Остаток: {product.quantity} шт."
                         for product in self.__products
                         )
