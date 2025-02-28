from typing import Generic, TypeVar, List, Optional, Collection


T = TypeVar('T')

class ArrayListADT(Generic[T]):
    def __init__(self, initial_capacity: int = 10) -> None:
        self._data: List[Optional[T]] = [None] * initial_capacity
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        new_data: List[Optional[T]] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def ensure_capacity(self, min_capacity: int) -> None:
        if len(self._data) < min_capacity:
            self._resize(min_capacity)

    def trim_to_size(self) -> None:
        self._resize(self._size)

    def add(self, e: T) -> bool:
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        self._data[self._size] = e
        self._size += 1
        return True

    def add_at(self, index: int, element: T) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = element
        self._size += 1

    def add_all(self, collection: Collection[T]) -> bool:
        for item in collection:
            self.add(item)
        return True

    def add_all_at(self, index: int, collection: Collection[T]) -> bool:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        for item in collection:
            self.add_at(index, item)
            index += 1
        return True

    def get(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]  # type: ignore

    def set(self, index: int, element: T) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        old_value = self._data[index]
        self._data[index] = element
        return old_value  # type: ignore

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        removed_element = self._data[index]  # type: ignore
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return removed_element

    def remove(self, o: T) -> bool:
        for index in range(self._size):
            if self._data[index] == o:
                self.remove_at(index)
                return True
        return False

    def clear(self) -> None:
        self._data = [None] * len(self._data)
        self._size = 0

    def contains(self, o: T) -> bool:
        for i in range(self._size):
            if self._data[i] == o:
                return True
        return False

    def index_of(self, o: T) -> int:
        for index in range(self._size):
            if self._data[index] == o:
                return index
        return -1

    def last_index_of(self, o: T) -> int:
        for index in range(self._size - 1, -1, -1):
            if self._data[index] == o:
                return index
        return -1

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"