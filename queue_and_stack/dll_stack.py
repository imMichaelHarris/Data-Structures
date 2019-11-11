import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList() 

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return value

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length


my_stack = Stack()
print(my_stack.push(1))
print(my_stack.push(2))
print(my_stack.push(3))
print(my_stack.size)
print(my_stack.pop())