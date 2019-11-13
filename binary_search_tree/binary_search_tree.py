import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is greater than the root value start a stack to the right if less go left
        # As going down tree check if current node is smaller or greater than value and then check if the node has a next to continue down the path
        # If node doesnt have a next on the side you need to traverse down then set the next to this value
        # start new tree
        new_tree = BinarySearchTree(value)
        if current.left != None and current.right != None:
            return
        elif value < self.value:
             # add to left
             self.left = value
        else:
            self.right = value
        insert()
        # if value < self.value:
        #     current = self.left
        #     while left is not None:
        #         left 
        #     self.left = new_tree
        # else:
        #     self.right = new_tree
        # return
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
