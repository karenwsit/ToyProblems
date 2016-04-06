"""
Find the height of a binary tree
"""

class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

def find_height(node, height=None):
    if node is None:
        return 0
    else:
        return max(find_height(node.left), find_height(node.right)) + 1

print find_height(root)