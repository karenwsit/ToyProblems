#Exercise 2.6 of Cracking the Coding Interview
#Implement a function to check if a linked list is palindrome
#################################################################################

#Time: O(n)
#Space:

#Solution 1: Reverse the linked list & compare the first half to the original linked list

def is_ll_palindrome(node):
    reversed_ll = reverse_ll(node)
    return is_equal(node, reversed_ll)

def reverse_ll(node):
    reversed_ll = node.reverse()
    return reversed_ll

def is_equal(node, reversed_node):
    p1 = node.head
    p2 = reversed_node.head

    while p1 is not None and p2 is not None:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    if p1 is not None or p2 is not None:
        return False
    else:
        return True


"""
Solution 2: Iterative Approach
-Reverse the 1st half of the list using a stack
-Iterate through 1st half of elements & push elements onto stack
    -Slow/fast runner technique
    -Elements from slow runner pushed to stack until fast runner reaches end of linked list
-Iterate through rest of the list to:
    -Compare node to the top of the stack
    -If we complete iteration without finding difference, ll is a palindrome
"""

def is_ll_palindrome2(node):
    slow = node.head
    fast = node.head

    stack = Stack()

    while fast != None and fast.next != None:
        stack.push(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast != None:  # an odd number linked list; skip middle element
        slow = slow.next

    while slow != None:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next

    return True
