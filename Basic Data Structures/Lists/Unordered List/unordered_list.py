from email.errors import NonPrintableDefect
from typing import Generic, TypeVar, Optional
from __future__ import annotations

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, init_data: T):
        self.data = init_data  # list item
        self.next = None  # Reference to next node

    # Define getters and setters for the fields

    def get_data(self) -> T:
        return self.data

    def get_next(self) -> Optional[Node[T]]:
        return self.next

    def set_data(self, data: T):
        self.data = data

    def set_next(self, next_node: Optional[Node[T]]):
        self.next = next_node


# TODO Implement append, insert, index, pop
# TODO If append is O(n), refactor so that it is O(1)


class UnorderedList(Node[T]):
    def __init__(self):
        self.head = None  # Head refers to the first item

    def is_empty(self) -> bool:
        return self.head == None  # If head is None, the list is empty

    def add(self, item: T) -> None:
        temp = Node(item)  # Create a new node with the item
        temp.set_next(self.head)  # Set next reference to the head
        self.head = temp

    def size(self) -> int:
        # Start from the head
        current = self.head
        count = 0
        # If current = None, we know that we reached the end of the list
        while current != None:
            count += 1
            # Traversing the list by getting the next references
            current = current.get_next()

        return count

    def search(self, item: T) -> bool:
        current = self.head
        found = False
        # Traverse until found or list is exhausted
        while not found and current != None:
            # If the node contents matches item to search for
            if current.get_data() == item:
                found = True
            else:
                # If not we go to next node
                current = current.get_next()

        return found

    def remove(self, item: T) -> None:
        current = self.head  # The current item in iteration
        prev = None  # The previous item visited
        found = False
        while not found:
            assert current != None  # Tell typechecker we know this will hold
            if current.get_data() == item:
                found = True
            else:
                prev = (
                    current  # Since we move one ahead, we set current to the previous
                )
                current = current.get_next()  # Move one ahead

        assert current != None  # Tell typechecker we know this will hold
        # If the previous is None, we have to start traversing
        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())


myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)

print(myList.size())
print(myList.search(17))
myList.remove(17)
print(myList.search(17))
