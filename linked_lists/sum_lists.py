#Exercise 2.5 of Cracking the Coding Interview
#You have 2 numbers represented by a linked list where each node contains a single digit. The digits are stored in reverse order such that the 1's digit is at the head of the list. Write a function that adds the 2 numbers and returns the sum as a linked list
#################################################################################

#Time = O(n)
#Space = O(1)

from linked_list import *

def sum_lists(node1, node2):
    """
    >>> from linked_list import *

    >>> ll = LinkedList()
    >>> ll.data_to_list([7,1,6])
    >>> ll2 = LinkedList()
    >>> ll2.data_to_list([5,9,2])
    >>> sum_lists(ll, ll2)
    LinkedList([2, 1, 9])
    """

    current1 = node1.head
    current2 = node2.head
    result_ll = LinkedList()  # result node
    tens_place = 0

    while current1 is not None and current2 is not None:
        sum1 = tens_place
        if current1 is not None:
            sum1 += current1.data
            current1 = current1.next
        if current2 is not None:
            sum1 += current2.data
            current2 = current2.next
        digit = sum1 % 10
        result_ll.addNode(digit)
        tens_place = sum1/10
        # sum1 % 10

    return result_ll

#################################################################################
#Recursive Solution

#Time: O(n)
#Space: O(n)

# def sum_lists2(node1, node2, carry=0):
#     """
#     >>> from linked_list import *
#     >>> ll = LinkedList()
#     >>> ll.data_to_list([7,1,6])
#     >>> ll2 = LinkedList()
#     >>> ll2.data_to_list([5,9,2])
#     >>> sum_lists2(ll, ll2)
#     LinkedList([2, 1, 9])
#     """
#     if node1 is None and node2 is None and carry == 0:
#         return None
#     result_ll = LinkedList()  # new node
#     value = carry

#     if node1 is not None:
#         value += node1.data
#     if node2 is not None:
#         value += node2.data

#     result.data = value % 10  # gets the ones' place digit

#     if node1 is not None or node2 is not None and value >= 10:
#         more = sum_lists2(node1.next, node2.next, carry == 1)
#     elif node1 is not None or node2 is not None and value < 10:
#         more = sum_lists2(node1.next, node2.next, carry == 0)

#     result.next = more

#     return result


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
