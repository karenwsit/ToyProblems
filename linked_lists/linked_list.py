class Node(object):
    """Singly linked list node representation"""

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node(%s)" % str(self.data)

class LinkedList(object):
    """Singly linked list implementation"""

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def size(self):
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.next

        return count

    def search(self, data):
        current = self.head
        found = False

        while current != None and not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found

    def remove(self, data):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.data == data:
                found = True
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
                current = current.next       

    def reverse(self):
        current = self.head
        previous = None

        while current != None:
            next = current.next
            current.next = previous #moving the link
            previous = current #resetting the pointers
            current = next
        self.head = previous


    def list_to_data(self):
        data_list = []
        current = self.head

        while current != None:
            data_list.append(current.data)
            current = current.next

        return data_list

    def data_to_list(self, data_list):
        self.head = Node(data_list[0])
        current = self.head

        for data in data_list[1:]:
            current.next = Node(data)
            current = current.next

    def __repr__(self):
        data_list = self.list_to_data()
        return "LinkedList(%s)" % str(data_list)

