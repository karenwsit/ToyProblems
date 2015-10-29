#Exercise 2.1 of Cracking the Coding Interview
#Write a method that removes duplicates in a linkedlist without using any temporary buffer.
#################################################################################

#Time = O(n)
#Space = O(1)

def return_k_to_last(k):
    p1 = ll.head
    p2 = ll.head

    for i in k:
        if p1 != None:
            p1 = p1.next

    while p1 != None:
        p1 = p1.next
        p2 = p2.next

    return p2


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()