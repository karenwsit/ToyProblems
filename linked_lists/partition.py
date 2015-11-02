#Exercise 2.4 of Cracking the Coding Interview
#Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x
#################################################################################

#Time = O(n)
#Space = O(1)

def partition(node, x):
    new_ll = LinkedList(node, node)
    node = node.next
    
    while node != None:
        new_node = Node(node.data)
        if new_node.data >= x:
            new_ll.tail.next = new_node
            new_ll.tail = new_node
        else:
            new_node.next = new_ll.head
            new_ll.head = new_node

    return new_ll

#################################################################################
#CTCI Solutions

def partition2(node, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while node != None:
        next = node.next
        node.next = None

        if node.data < x:
            if before_start == None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            #(node.data >= x)
            if after_start == None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node

        node = next

    if before_start == None:
        return after_start

    before_start.next = after_start
    return before_start

def partition3(node, x):
    head = None
    tail = None

    while node!= None:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    tail.next = None

    return head
