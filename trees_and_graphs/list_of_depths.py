"""
CTCI 4.3: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
(E.g. If you have a tree with depth D, you'll have D linked lists)
"""

class BinaryTree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LinkedList(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_tree_to_list_of_ll(btree, depth=1, result=[]):
    if len(result) >= depth:
        ll = LinkedList(btree.value)
        ll.next = result[depth-1]
        result[depth-1] = ll
    else:
        result.append(LinkedList(btree.value))
    if btree.left:
        result = binary_tree_to_list_of_ll(btree.left, depth+1, result)
    if btree.right:
        result = binary_tree_to_list_of_ll(btree.right, depth+1, result)
    return result

# Breadth First Search Using a Queue

def binary_tree_to_list_of_ll2(btree):
    if btree is None:
        return []
    result = [[btree.value]]
    queue = [btree]
    while queue:
        new_queue = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
        if len(queue) == 0:
            break
        result.append([x.value for x in queue])
    return result


