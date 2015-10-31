#Exercise 2.2 of Cracking the Coding Interview
#Implement an algorithm to find the kth to last element of a singly linked list
#################################################################################

#Time = O(n)
#Space = O(1)

def k_to_last(node, k):
    """
    >>> from linked_list import *

    >>> ll_example = LinkedList()
    >>> ll_example.data_to_list([1,3,3,2,4,6,4,6,3])
    >>> ll_example_result = k_to_last(ll_example.head, 3)
    >>> ll_example_result
    Node(4)

    >>> ll_example2 = LinkedList()
    >>> ll_example2.data_to_list([0,1,2])
    >>> ll_example2_result = k_to_last(ll_example2.head, 5)
    >>> ll_example2_result

    >>> ll_example3 = LinkedList()
    >>> ll_example3.data_to_list([1,2,3,4])
    >>> ll_example3_result = k_to_last(ll_example3.head, 4)
    >>> ll_example3_result
    Node(1)
    """

    p1 = node
    p2 = node
    counter = 0

    while p1 != None:
        p1 = p1.next
        counter += 1
        if counter > k:
            p2 = p2.next

    if counter < k:
        return None
    return p2

#Recursive Solution
#Time:
#Space: O(n)

# def k_to_last2(node, k):
#     if node = None:
#         return 0

#     index = k_to_last2(node.next, k) + 1

#     if index == k:
#         print k + "th to the last node is " + node.data

#     return index

#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()