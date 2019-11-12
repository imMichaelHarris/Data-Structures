from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.

    Sounds like a queue
    When a pair is updated or newly set the other pairs in cache is now one spot lower (array sounds good here)
    If cache is at maximum lowest gets removed
    If key exists overwrite 
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.dll = DoublyLinkedList()
        # fast access sounds like array
        self.storage = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if hasattr(self.storage, key):
            # move to end of linkedlist
            return getattr(self.storage, key)
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        pass

    
my_cache = LRUCache()
print(my_cache.dll.add_to_tail(10))
print(my_cache.dll.add_to_tail(4))
print(my_cache.dll.add_to_tail(25))
print(my_cache.dll.add_to_tail(14))

# print(my_cache.storage)