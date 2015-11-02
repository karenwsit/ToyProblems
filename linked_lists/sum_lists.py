#Exercise 2.5 of Cracking the Coding Interview
#You have 2 numbers represented by a linked list where each node contains a single digit. The digits are stored in reverse order such that the 1's digit is at the head of the list. Write a function that adds the 2 numbers and returns the sum as a linked list
#################################################################################

#Time = O(n)
#Space = O(1)

def sum_lists(node1, node2):
    current1 = node1.head
    current2 = node2.head
    linkedlist_result = LinkedList()  # result node
    head is None
    tens_place = 0

    while current1 is not None and current2 is not None:
        sum = str(current1.data + current2.data + tens_place)
        if len(sum) > 1:
            tens_place = sum[-2]
        ones_place = sum[-1]
        linkedlist_result.next = ones_place
        head = result
        result = ones_place

        current1 = current1.next
        current2 = current2.next

    return head

#################################################################################
#Recursive Solution

#Time: O()
#Space: O()

def sum_lists2(node1, node2, carry):
    if node1 is None and node2 is None and carry == 0:
        return None
    result = None  # new node
    more = None  # new node

    value = carry

    if node1 is not None:
        value += node1.data
    if node2 is not None:
        value += node2.data

    result.data = value % 10  # gets the ones' place digit

    if node1 is not None or node2 is not None and value >=10:
        more = sum_lists2(node1.next, node2.next, carry == 1)
    elif node1 is not None or node2 is not None and value < 10:
        more = sum_lists2(node1.next, node2.next, carry == 0)

    result.next(more)

    return result

#################################################################################
# Follow Up
#Reverse each of the linked lists & put them into sum_lists2. 
