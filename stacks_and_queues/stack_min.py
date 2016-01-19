#Exercise 3.2 of Cracking the Coding Interview
#How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
#################################################################################

class StackWithMin(object):
    
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, value):
        self.items.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def get_minimum(self):
        if len(self.min) == 0:
            return None
        return self.min[-1]
