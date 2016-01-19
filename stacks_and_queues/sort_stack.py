#Exercise 3.5 of Cracking the Coding Interview
#Write a program to sort a stack such that the smallest items are on the top.
#You can use an additional temporary stack, but you may not copy the elements
#into any other data structure. The stack supports the following operations: push, pop, peek, isEmpty.

#################################################################################

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def sort_stack(s):
        r = Stack()
        while not s.is_empty():
            temp = s.pop()
            while not r.is_empty() and r.peek() > temp:
                s.push(r.pop())
            r.push(temp)
            while not s.is_empty() and s.peek() >= r.peek():
                r.push(s.pop())
        return r
        