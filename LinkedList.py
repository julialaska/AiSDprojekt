from typing import Any


class Node:
    value: Any
    next: None

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head: None = None
        self.tail: None = None

    def push(self, value: Any) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, value: Any) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = node

    def node(self, at: int) -> Node:
        i = 0
        node = self.head
        while True:
            if i == at:
                return node.value
            i += 1
            node = node.next

    def insert(self, value: Any, after: Node) -> None:
        new = Node(value)
        temp = self.head
        while temp is not None:
            if temp.value == after:
                new.next = temp.next
                temp.next = new
            temp = temp.next

    def pop(self) -> Any:
        if self.head is None:
            return None
        else:
            tmp = self.head.value
            self.head = self.head.next
            return tmp

    def remove_last(self) -> Any:
        last = self.head
        while last.next.next is not None:
            last = last.next
        tmp = last.next
        last.next = None
        return tmp.value

    def remove(self, after: Node) -> Any:
        head = self.head

        while head.next is not None:
            if head.next.value == after:
                head = head.next
            head.next = head.next.next

    def print(self):
        element = self.head
        while element is not None:
            print(element.value, end="->")
            element = element.next
        print("None")

    def len(self):
        length = 0
        pom = self.head
        while pom is not None:
            length += 1
            pom = pom.next
        return length

    def __len__(self):
        length = 0
        pom = self.head
        while pom is not None:
            length += 1
            pom = pom.next
        return length

    def __str__(self):
        node = self.head
        st = " ->"
        wynik: str = str(node.value)
        while node.next is not None:
            wynik += st + ' ' + str(node.next.value)
            node = node.next
        return wynik


list_ = LinkedList()
assert list_.head is None

list_.push(1)
list_.push(0)

print(list_)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

print(list_)

middle_node = list_.node(at=1)
print(middle_node)
list_.insert(5, after=middle_node)
#
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

print(list_)

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element == returned_first_element

print(list_)

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

print(len(list_))
