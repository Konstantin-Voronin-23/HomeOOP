import unittest

from src.iterators import CategoryIterator


class TestCategoryIterator(unittest.TestCase):
    def setUp(self):

        class MockCategory:
            def __init__(self, products):
                self.products = products

        self.mock_category = MockCategory(["product1", "product2", "product3"])

    def test_iterator_returns_all_products(self):
        """Проверка на то, что корректно возвращаются все продукты"""
        iterator = CategoryIterator(self.mock_category)
        products = list(iterator)
        self.assertEqual(products, ["product1", "product2", "product3"])

    def test_iterator_stops_after_last_product(self):
        """Проверка, что после последнего продукта итератор останавливается"""
        iterator = CategoryIterator(self.mock_category)

        next(iterator)
        next(iterator)
        next(iterator)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_empty_category(self):
        """Проверка пустого знеачения"""
        empty_category = type('', (), {'products': []})()
        iterator = CategoryIterator(empty_category)
        with self.assertRaises(StopIteration):
            next(iterator)
        self.assertEqual(list(iterator), [])

    def test_iterator_is_iterable(self):
        """Проверяет, что объект CategoryIterator является корректным итерируемым объектом"""
        iterator = CategoryIterator(self.mock_category)
        self.assertTrue(hasattr(iterator, '__iter__'))
        self.assertIs(iter(iterator), iterator)
