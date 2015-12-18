"""
CTCI 4.4: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two node never differ by more than one
"""

def height(node):

    # Base Case
    if node == None:
        return 0

    


def is_bt_balanced(node):

    # Base Case
    if node == None:
        return True

    if abs(depth(node.left) - depth(node.right)) > 1:
        return False

    return is_bt_balanced(node.left) and is_bt_balanced(node.right)