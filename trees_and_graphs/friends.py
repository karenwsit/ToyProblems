"""Find whether two people in an undirected graph are friends.

"""

class PersonNode(object):
    """A node in a graph representing a person.
    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
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


        """
    def __init__(self):
        """Create an empty graph.
        We will keep a dictionary to map people's names to nodes
        """
        self.nodes = {}

    def add_person(self, name):
        """Add a person to our graph.

        >>> f = FriendGraph()
        >>> f.nodes
        {}

        >>> f.add_person("Dumbledore")
        >>> f.nodes
        {'Dumbledore: <PersonNode Dumbledore>'}
        """
        if name not in self.nodes:
            self.nodes[name] = PersonNode(name)
