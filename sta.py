from LinkedList import LinkedList
from typing import Any


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()

    def len(self):
        return len(self._storage)

    def print(self):
        node = self._storage.head
        while node is not None:
            print(str(node.value))
            node = node.next

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        for i in range(0, self._storage.len()):
            return str(self._storage)


stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

stack.print()

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2
