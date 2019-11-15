import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # A DLL is good because with it we can change the head and tail with good time complexity O(1)
        # self.storage = ?
        self.queue_list = DoublyLinkedList()

    def enqueue(self, value):
        if self.size == 0:
            self.queue_list.add_to_tail(value)
        else:
            self.queue_list.add_to_tail(value)

        self.size += 1
        
        

    def dequeue(self):
        if self.size == 0:
            return
        else:
            return self.queue_list.remove_from_head()

    def len(self):
        return self.queue_list.length

# my_queue = Queue()
# print(my_queue.enqueue(1))
# print(my_queue.enqueue(2))
# print(my_queue.enqueue(3))
# print(my_queue.size)
# print(my_queue.dequeue())