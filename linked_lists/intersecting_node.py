#Exercise 2.7 of Cracking the Coding Interview
#Given 2 singly linked lists, deterine if the 2 lists intersect. Return the intersecting node.
#Note that the intersection is defined based on reference, not value.
#That is, if the kth node of the 1st linked list is the exact same node as the jth node of the second linked list, then they are intersecting
#################################################################################

#Initial Naive Solution (not shown): Reverse the linked lists and traverse backwards. Cannot reverse linked lists when reversing linked list 1, will alter linkedlist2

#Time: O(m*n)
#Space: O(1)

from linked_list import *

def intersecting_node(ll1, ll2):
    """
    Nested for loops

    >>> ll1 = LinkedList()
    >>> ll1.data_to_list([3, 6, 9, 15, 30])
    >>> ll2 = LinkedList()
    >>> ll2.data_to_list([10, 15, 30])
    >>> intersecting_node(ll1, ll2)
    Node(15)
    """
    current1 = ll1.head
    current2 = ll2.head

    while current1 != None:
        while current2 != None:
            if current1.data == current2.data:
                return current1
            current2 = current2.next
        current2 = ll2.head
        current1 = current1.next

    return None

# CTCI Interview Solution
# """
# 1. Run through each linked list to get lengths & tails
# 2. Compare tails (by reference not value). If different, return False - do not intersect
# 3. Set 2 pointers @ start of each linked list
# 4. On longer linked list, advance pointer by diff of lengths
# 5. Traverse until pointers are the same
# """

def intersecting_node2(ll1, ll2):
    """
    >>> ll1 = LinkedList()
    >>> ll1.data_to_list([3, 6, 9, 15, 30])
    >>> ll2 = LinkedList()
    >>> ll2.data_to_list([10, 15, 30])
    >>> intersecting_node(ll1, ll2)
    Node(15)
    """

    current1 = ll1.head
    current2 = ll2.head
    len1 = 0
    len2 = 0

    while current1 != None:
        len1 += 1
        current1 = current1.next
    while current2 != None:
        len2 += 1
        current2 = current2.next

    if current1 is not current2:
        return False  # there is no intersection

    current1 = ll1.head
    current2 = ll2.head

    if len1 > len2:
        for i in range(len1-len2):
            current1 = current1.next
    elif len2 > len1:
        for i in range(len2-len1):
            current2 = current2.next
    while current1.data != current2.data:
        current1 = current1.next
        current2 = current2.next
    return current1


#########################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    
