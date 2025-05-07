

class Product():
    """Класс для названия и описания продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации класса"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
