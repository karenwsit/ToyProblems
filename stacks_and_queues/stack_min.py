#Exercise 3.2 of Cracking the Coding Interview
#How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
#################################################################################

class StackWithMin(object):
    
    def __init__(self, minimum=None, second_minimum=None):
        self.items = []
        self.minimum = minimum
        self.second_minimum = second_minimum

    def push(self, value):
        self.items.append(value)
        if value < minimum:
            minimum = value


    def pop(self):
        return self.items.pop()

    def get_minimum(self):


USE ANOTHER AUXILLARY STACK TO STORE MIN VALUES of every state of the stack