#Exercise 3.4 of Cracking the Coding Interview
#Implement a MyQueue class which implements a queue using two stacks

#################################################################################

class myQueue(object):
    
    def __init__(self):
        self.front_stack = Stack()
        self.back_stack = Stack()

    def enqueue(self, value):
        self.back_stack.push(value)

    def dequeue(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.pop()

    def rebuild(self):
        while self.back_stack.size > 0:
            self.front_stack.push(self.back_stack.pop())

    def peek_front(self):
        if self.front_size.size == 0:
            self.rebuild
        return self.front_size.peek()

