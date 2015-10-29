#Exercise 2.1 of Cracking the Coding Interview
#Write a method that removes duplicates in a linkedlist without using any temporary buffer.
#################################################################################

#Time = O(n)
#Space = O(n)

def remove_duplicates(ll):
    """
    >>> from linkedlist import *

    >>> ll_example = LinkedList()
    >>> ll_example.data_to_list([1,3,3,2,4,6,4,6,3])
    >>> ll_example_result = remove_duplicates(ll_example)
    >>> ll_example_result
    LinkedList([1,3,2,4,6])

    >>> ll_example2 = LinkedList()
    >>> ll_example2.data_to_list([0,1,2])
    >>> ll_example2_result = remove_duplicates(ll_example2)
    >>> ll_example2_result
    LinkedList([0,1,2])

    >>> ll_example3 = LinkedList()
    >>> ll_example3.data_to_list([1,1,2,3])
    >>> ll_example3_result = remove_duplicates(ll_example3)
    >>> ll_example3_result
    LinkedList([1,2,3])
    """

    data_set = set()
    current = ll.head
    previous = None

    while current != None:
        if current.data in data_set:
            previous.next = current.next
            current = previous.next
        else:
            data_set.add(current.data)
            previous = current
            current = current.next
    return ll



#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
