"""Find whether two people in an undirected graph are friends.

"""

class PersonNode(object):
    """A node in a graph representing a person.
    This is created with a name and, optionally, a list of adjacent nodes.""""

    def __init__(self, name, adjacent= []):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name


class FriendGraph(object):
    """Graph to keep track of social connections. Let's create a graph and add a bunch of people.

        >>> f = FriendGraph()
        >>> f.add_person('Frodo')
        >>> f.add_person('Sam')
        >>> f.add_person('Gandalf')
        >>> f.add_person('Merry')
        >>> f.add_person('Pippin')
        >>> f.add_person('Treebeard')
        >>> f.add_person('Sauron')
        >>> f.add_person('Dick Cheney')

        