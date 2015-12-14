"""
CTCI 4.2: Given a sorted (increasing order) array with unique integer elements, write an alogirthm to create a binary search tree with minimal height
"""

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def make_bst(nums, left, right):
    node_index = len(nums)/2
    node = nums[node_index]

    left_subtree = nums[0:node_index]
    right_subtree = nums[node_index:]

    if len(left_subtree) == 1:
        node.left = left_subtree[0]
    if len(right_subtree) == 1:
        node.right = right_subtree[0]

    left = make_bst(left_subtree)
    right = make_bst(right_subtree)