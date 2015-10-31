#Exercise 2.3 of Cracking the Coding Interview
#Implement an algorithm to delete a node in the middle of a singly linked list given only access to that node
#################################################################################

#Time = O(n)
#Space = O(1)

def delete_middle(node):
    current = node
    if current.next == None or current == None:
        return False
    next = current.next
    current.data == next.data
    current.next == next.next
    return True

    #if node to be deleted is the last node, cannot solve
    #if node is @ the end; ask interviewer how to handle this



