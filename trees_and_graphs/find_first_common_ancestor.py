"""
CTCI 4.8: First Common Ancestor: Design an algorithm and write code to find the first common ancestor of 2 nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
"""

class BinaryTreeNode(object):

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_first_common_ancestor(p, q):
    if p is None or q is None:
        return None
    if is_descendent(p, q):
        return p
    current = p
    parent = current.parent
    


# check if n is a descendent of root
def is_descendent(root, n):
    if root is None:
        return False
    if root is n:
        return True
    return is_descendent(root.left, n) or is_descendent(root.right, n)
