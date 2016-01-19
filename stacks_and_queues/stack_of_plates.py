#Exercise 3.3 of Cracking the Coding Interview
#Implement a data structure SetofStacks that micmics starting a new stack when the previous stack exceeds some threshold.
#SetofStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
#SetofStacks.push() and SetofStacks.pop() should behave identically to a single stack.
#################################################################################

#Nested lists as a solution

class SetofStacks(object):
    
    def __init__(self, threshold=100):
        self.threshold = threshold
        self.items = []

    def push(self, value):
        if len(self.items) == 0 or len(self.items[-1]) == self.threshold:
            self.items.append([])
        self.items[-1].append(value)

    def pop(self):
        if len(self.items) == 0:
            return None 
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.items.pop()
        return data

    #Index starts at 0
    def pop_at(self, index):
        if index+1 < 1 or index+1 > len(self.stacks) or len(self.stacks[index]) == 0:
            return None
        else:
            return self.stacks[index].pop()


