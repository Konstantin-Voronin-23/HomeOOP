from typing import Any, Dict, List, Optional


class Product():
    """Класс для названия и описания продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Метод отображения информации об объекте класса для пользователя"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: Dict, products_list: Optional[List['Product']] = None) -> 'Product':
        """Принимает на вход параметры товара в словаре и возвращать созданный объект класса"""

        if products_list is None:
            products_list = []

        for product in products_list:
            if product.name.lower() == product_data['name'].lower():
                product.quantity += product_data['quantity']
                if product_data['price'] > product.price:
                    product.__price = product_data['price']
                return product

        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __add__(self, other: Any) -> Any:
        """Метод сложения продуктов, считающий их полную стоимость"""

        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if self.__class__ is not other.__class__:
            raise TypeError("Нельзя складывать товары разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        """Getter возвращает значение приватного атрибута цены"""

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Setter проверяет: в случае если цена равна или ниже нуля, выводит сообщение в консоль"""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, '_Product__price') and new_price < self.__price:
            user_choice = input(
                f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ").lower()
            if user_choice != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price


class Smartphone(Product):
    """Класс с описанием смартфонов"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс с описанием газонной травы"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
