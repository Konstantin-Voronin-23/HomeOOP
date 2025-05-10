from src.Category import Category
from src.Product import Product

import json

import pytest


@pytest.fixture(autouse=True)
def reset_category_state():
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def temp_json_file(tmp_path):
    """Создает временный JSON файл для тестов"""
    file_path = tmp_path / "test.json"
    data = [
        {
            "name": "Электроника",
            "description": "Техника для дома",
            "products": [
                {"name": "Телефон", "description": "Смартфон", "price": 50000.0, "quantity": 10},
                {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000.0, "quantity": 5}
            ]
        }
    ]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными"""
    return [
        {
            "name": "Электроника",
            "description": "Техника для дома",
            "products": [
                {"name": "Телефон", "description": "Смартфон", "price": 50000.0, "quantity": 10},
                {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000.0, "quantity": 5}
            ]
        }
    ]
