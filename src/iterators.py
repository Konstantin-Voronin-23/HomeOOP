from typing import Any, Iterator


class CategoryIterator:
    def __init__(self, category: Any) -> None:
        self._category = category
        self._index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        raise StopIteration
