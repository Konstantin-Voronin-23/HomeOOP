

class Product():
    """Класс для названия и описания продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
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
