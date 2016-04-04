#Exercise 4.5 Cracking the Coding Interview
#Implement a function to check if a binary tree is a binary search tree
#################################################################################

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node):
    l = in_order_search(node)
    if l == sorted(l):
        return True
    return False

def in_order_search(node, sorted_array=None):
    if sorted_array is None:
        sorted_array = []
    if node is None:
        return []
    while node:
        in_order_search(node.left)
        sorted_array = sorted_array.append(node.value)
        in_order_search(node.right)
    return sorted_array
