"""
CTCI 4.2: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height
"""

class BinarySearchTree(object):
    def __init__(self, content, left=None, right=None):
        self.content = content
        self.left = left
        self.right = right

def make_minimal_tree_from_sorted_array(sorted_array):

    if len(sorted_array) == 0:
        return None

    if len(sorted_array) == 1:
        return BinarySearchTree(sorted_array[0])

    middle = len(sorted_array) // 2

    return BinarySearchTree(sorted_array[middle],
        make_minimal_tree_from_sorted_array(sorted_array[0:middle]),
        make_minimal_tree_from_sorted_array(sorted_array[middle+1:]))
