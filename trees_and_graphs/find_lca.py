"""
Find Lowest Common Ancestor in a BST
http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
"""
 
# A Binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_lca_bst(node, n1, n2):
    #base case
    if node is None:
        return None

    if n1 > n2:
        n1 = n2
        n2 = n1

    if n1 < node.data and n2 < node.data:
        find_lca_bst(node.left, n1, n2)
    elif n > node.data and n2 > node.data:
        find_lca_bst(node.right, n1, n2)
    else:
        return node

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)