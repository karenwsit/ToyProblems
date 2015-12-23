"""
CTCI 4.4: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two node never differ by more than one
"""

class BinaryNode(object):
    """Node in binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def height(node):

    # Base Case
    if node == None:
        return 0

    return max(height(node.left), height(node.right)) + 1  # Unsure why we need to add 1


def is_bt_balanced(node):
    """
    >>> N = BinaryNode
    >>> tree1 = N(1)
    >>> tree1.is_bt_balanced()
    True

    >>> tree2 = N(1, N(2))
    >>> tree2.is_bt_balanced()
    True

    >>> tree3 = N(1, N(2), N(3))
    >>> tree3.is_bt_balanced()
    True

    >>> tree4 = N(1, N(2, N(3)), N(4))
    >>> tree4.is_bt_balanced()
    True

    >>> tree5 = N(1, N(2, N(3), N(4)), N(5))
    >>> tree5.is_bt_balanced()
    True

    >>> tree6 = N(1, N(2, N(3), N(4)))
    >>> tree6.is_bt_balanced()
    False
    """

    # Base Case
    if node == None:
        return True

    if abs(depth(node.left) - depth(node.right)) > 1:
        return False

    return is_bt_balanced(node.left) and is_bt_balanced(node.right)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
