#Exercise 4.5 Cracking the Coding Interview
#Implement a function to check if a binary tree is a binary search tree
#################################################################################

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Runtime: O(n)
#Space: O(n)
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

    in_order_search(node.left, sorted_array)
    sorted_array.append(node.value)
    in_order_search(node.right, sorted_array)
    return sorted_array

#Min & Max Solution
#Runtime:O(n)
#Space: O(log n) on a balanced tree
def is_bst2(root, maxi, mini):
    if root is None:
        return True
    elif (mini is not None and root.value <= mini) or (maxi is not None and root.value > maxi):
        return False
    elif is_bst2(root.left, mini, root.value) == False or is_bst2(root.right, root.value, maxi) == False:
        return False
    return True

#TESTING
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(0)
root.left.right = Node(3)
root.left.left.right = Node(1)
root.right.right = Node(8)

print in_order_search(root)
print is_bst2(root, None, None)
