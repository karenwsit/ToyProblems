class HashTable():
    def __init__(self):
        self.size = 11  # arbitrary number but needs to be a prime # so collision resolution algorithm is most efficient
        self.slots = [None] * self.size  # hold the key items
        self.data = [None] * self.size  # hold the value items

def put(self, key, data):
    """
    Assumes there will eventually be an empty slot unless key is already present in self.slots
    Computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs
    If a nonempty slot already contains the key, old data value replaced with new data value
    """
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
    else:
        if self.slots[hashvalue] == key:
            self.data[hashvalue] = data  # replace data
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data  # replace data
def hashfunction(self, key, size):
    return key % size

def rehash(self, oldhash, size):
    return (oldhash+1) % size