#Exercise 3.1 of Cracking the Coding Interview
#Describe how you could use a single array to implement three stacks.
#################################################################################

class SingleArrayStacks(object):

    def __init__(self, stacksize=100, number=3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number   # [None, None, None...etc.]
        self.pointer = [-1] * self.number  # [-1,-1,-1]

    def push(self, stacknum, value):
        