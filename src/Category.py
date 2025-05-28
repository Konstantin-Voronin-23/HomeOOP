from typing import Any, Iterator, List

from src.iterators import CategoryIterator
from src.Product import Product


class Category():
    """Класс для названия и описании категорий"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List['Product'] = None) -> None:
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""

        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты от класса Product")

        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Метод отображения информации о категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Возвращает строковое представление товаров"""

        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __iter__(self) -> Iterator[Any]:
        return CategoryIterator(self)

    @property
    def products(self) -> List[Any]:
        return self.__products

    def get_average_prices(self):
        """Подсчитывает средний ценник всех товаров"""

        try:
            total_price = sum(product.price for product in self.__products)
            avg = total_price / len(self.__products)
            return avg
        except ZeroDivisionError:
            return 0
        except AttributeError:
            print("Ошибка: у некоторых товаров отсутствует цена (атрибут price)")
            return 0
        except TypeError:
            print("Ошибка: цена товара должна быть числом")
            return 0
