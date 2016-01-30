#Exercise 4.6 of Cracking the Coding Interview
#Write an algorithm to fint the  'next' node (i.e., in-order successor) of a given node in a binary search btre.
#You may assume that each node has a link to its parent.
#################################################################################

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_succssor(btree):
    if btree is None:
        return None
    if btree.right:
        successor = find_min(btree.right)
    else:
        successor = btree.parent
        while btree.parent is not None and successor.value <= btree.value:
            successor = successor.parent
    return successor


def find_min(btree):
    if btree is None:
        return None
    while btree.left:
        successor = btree.left
    return successor