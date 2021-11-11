from LinkedList import LinkedList
from typing import Any


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __len__(self):
        return len(self._storage)

    def print(self):
        print(self._storage)

    def __str__(self):
        node = self._storage.head
        st = ","
        wynik: str = str(node.value)
        while node.next is not None:
            wynik += st + ' ' + str(node.next.value)
            node = node.next
        return wynik


queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
queue.print()
print(queue)

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
