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
    """
    >>> find_lca_bst(node, 10, 14)
    12
    >>> find_lca_bst(node, 14, 8)
    8
    >>> find_lca_bst(node, 10, 22)
    20
    """
    #base case
    if node is None:
        return None

    if n1 < node.data and n2 < node.data:
        return find_lca_bst(node.left, n1, n2)
    if n1 > node.data and n2 > node.data:
        return find_lca_bst(node.right, n1, n2)
    return node.data

node = Node(20)
node.left = Node(8)
node.right = Node(22)
node.left.left = Node(4)
node.left.right = Node(12)
node.left.right.left = Node(10)
node.left.right.right = Node(14)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
