

class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        raise StopIteration

