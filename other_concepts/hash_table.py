class HashTable():
    def __init__(self):
        self.size = 11  # arbitrary number but needs to be a prime # so collision resolution algorithm is most efficient
        self.slots = [None] * self.size  # hold the key items
        self.data = [None] * self.size  # hold the value items


