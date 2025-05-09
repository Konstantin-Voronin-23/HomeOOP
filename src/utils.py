import json

from src.Category import Category
from src.Product import Product


def read_json_file(path: str) -> list[dict]:
    """Функция для чтения json файла"""

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as error:
        print(f"Ошибка: файл {error.filename} не найден! ")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {path} содержит некорректный JSON! ")
        return []


def create_object_from_json(data: list[dict]):
    """Функция которая принимает Json файл и превращает категории в объекты"""

    return [
        Category(
            name=category["name"],
            description=category["description"],
            products=[Product(**product) for product in category["products"]]
        )
        for category in data
    ]
