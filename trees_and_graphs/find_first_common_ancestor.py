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

    while parent:
        if (parent is q) or (parent.left is current and is_descendent(parent.right, q)) or (parent.right is current and is_descendent(parent.left, q)):
            return parent
        current = parent
        parent = current.parent
    return None


# check if n is a descendent of root
def is_descendent(root, n):
    if root is None:
        return False
    if root is n:
        return True
    return is_descendent(root.left, n) or is_descendent(root.right, n)


"""
Design an algorithm and write code to find the first common ancestor of 2 nodes in a binary tree.
A data structure can be used to store the nodes
#Runtime: O(n) solution to find LCS of two given values n1 and n2
"""

class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def find_lca(root, n1, n2):
    """
    >>> find_lca(root, 4, 5)
    2
    >>> find_lca(root, 4, 6)
    1
    >>> find_lca(root, 3, 4)
    1
    """
    #base case
    if root is None:
        return None

    path1 = []
    path2 = []

    #find paths from root to n1 and root to n2
    #if neither n1 or n2 is present, return -1
    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


def find_path(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return path
    if (root.left != None and find_path(root.right, path, k)) or (root.right != None and find_path(root.left, path, k)):
        return True
    path.pop()

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
