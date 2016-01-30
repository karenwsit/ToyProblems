#Exercise 4.1 of Cracking the Coding Interview
#Given a directed graph, design an algorithm to find out whether there is a path route between two nodes
#################################################################################

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(btree, sorted_array=[]):
    l = in_order_search(btree)
    if l == sorted(l):
        return True
    return False

def in_order_search(btree):
    if btree is None:
        return []
    while btree:
        in_order_search(btree.left)
        sorted_array = sorted_array.append(btree.value)
        in_order_search(btree.right)
    return sorted_array
