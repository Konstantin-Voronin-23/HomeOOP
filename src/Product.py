

class Product():
    """Класс для названия и описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
