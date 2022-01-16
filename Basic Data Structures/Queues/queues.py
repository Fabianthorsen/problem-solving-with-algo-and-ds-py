from typing import Generic, TypeVar, List

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def is_empty(self) -> bool:
        return self.items == []

    def enqueue(self, item: T) -> None:
        self.items.insert(0, item)  # Insert at the rear

    def dequeue(self) -> T:
        return self.items.pop()  # Pop front of queue

    def size(self) -> int:
        return len(self.items)


q = Queue[str]()
q.enqueue("Hello")
q.enqueue("dog")
# q.enqueue(3) # Error since it is a Queue of strings
print(q.size())
print(q.dequeue())
print(q.size())
