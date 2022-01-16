from typing import Generic, TypeVar

T = TypeVar("T")


class Deque(Generic[T]):
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    # This operation is O(1)
    def add_front(self, item: T) -> None:
        self.items.append(item)

    # This operation is O(n)
    def add_rear(self, item: T) -> None:
        self.items.insert(0, item)

    # This operation is O(1)
    def remove_front(self) -> T:
        return self.items.pop()

    # This operation is O(n)
    def remove_rear(self) -> T:
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)
