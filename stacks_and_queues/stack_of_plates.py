#Exercise 3.3 of Cracking the Coding Interview
#Implement a data structure SetofStacks that micmics starting a new stack when the previous stack exceeds some threshold.
#SetofStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
#SetofStacks.push() and SetofStacks.pop() should behave identically to a single stack.
#################################################################################

#Nested lists as a solution? Yes!

class SetofStacks(object):
    
    def __init__(self, threshold=100):
        self.threshold = threshold
        self.items = []

    def push(self, value):
        if len(self.items) > threshold:
            self.items.append([])
            sub_stack.append(value)
        else:
            self.items.append(value)

    def pop(self):
        if len(self.items) > threshold:
            new_stack = Stack()
            new_stack.append(value)
        else:
            return self.items.pop()

