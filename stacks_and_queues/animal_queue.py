#Exercise 3.6 of Cracking the Coding Interview
#An animal shelther which holds only cats & dogs operatoes on a strictly FIFO basis.
#People must adopt either the oldest of all animals at the shelter or they can select whether they would prefer a dog or a cat.
#They cannot select which specific animal they would like. Create the data structures to maina these system.
#Implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
#################################################################################

class AnimalQueue(object):
    def __init__(self):
        from collections import deque
        self.dog_q = deque()
        self.cat_q = deque()
        self.time_stamp = 0

    def enqueue(self, animal_type, animal_name):
        if animal_type == "dog":
            self.dog_q.appendleft((animal_name, self.time_stamp))
            self.time_stamp += 1
        elif animal_type == "cat":
            self.cat_q.appendleft((animal_name, self.time_stamp))
            self.time_stamp += 1
        else:
            print "invalid animal type"

    def dequeue_any(self):
        dog = self.dog_q.pop() if not len(self.dog_q) == 0 else (None, -1)
        cat = self.cat_q.pop() if not len(self.cat_q) == 0 else (None, -1)

        if dog[1] == -1 and cat[1] == -1:
            return None
        elif dog[1] < cat[1]:
            self.cat_q.append(cat)
            return dog[0]
        else:
            self.dog_q.append(dog)
            return cat[0]

    def dequeue_cat(self):
        if not len(self.cat_q) == 0:
            return self.cat_q.pop()[0]

    def dequeue_dog(self):
        if not len(self.dog_q) == 0:
            return self.dog_q.pop()[0]
