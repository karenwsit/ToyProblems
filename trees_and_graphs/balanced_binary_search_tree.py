"""
CTCI 4.2: Given a sorted (increasing order) array with unique integer elements, write an alogirthm to create a binary search tree with minimal height
"""

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def make_bst(nums):

    # Base case when there is no more integers in the array
    if not nums:
        return None

    mid_index = len(nums)/2

    # Make a new node out of the midpoint of array
    node = BinaryNode(nums[mid_index])

    node.left = make_bst(nums[:mid_index])
    node.right = make_bst(nums[mid_index + 1:])

    return node
    