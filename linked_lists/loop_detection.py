#Exercise 2.8 of Cracking the Coding Interview
#Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
#################################################################################

#Use Floyd's cycle-finding algorithm

#Time = O(n)
#Space = O(1)

def loop_detection(ll):
    if ll is None:
        return False

    slow = ll.head
    fast = ll.head

    if slow.next == None or fast.next == None:
        return False

    while fast != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None
