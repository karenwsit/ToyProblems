#Exercise 4.12 of Cracking the Coding Interview
#You are given a binary tree in which each node contains an integer value (which can be positive/negative)
#Design an algorithm to count the # of paths that sum to a given value. The path does not need to start/end at the root or a leaf, but it must go downwards.
#################################################################################

#Runtime: O(n log n) for a balanced tree; O(n^2) on an unbalanced tree

class binaryTree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_paths_with_sum(node, target_sum):
    if node is None:
        return 0

    paths_from_root = count_paths_with_sum_from_node(node, target_sum, current_sum)

    paths_from_left = count_paths_with_sum(node.left, target_sum)
    paths_from_right = count_paths_with_sum_from_node(node.right, target_sum)

    return paths_from_root + paths_from_left + paths_from_right

def count_paths_with_sum_from_node(node, target_sum, current_sum):
    if node is None:
        return 0

    current_sum += node.value
    total_paths = 0
    if current_sum == target_sum:
        total_paths += 1

    total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
    total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)

    return total_paths
