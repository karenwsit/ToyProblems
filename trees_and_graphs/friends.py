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
        {'Dumbledore': <PersonNode Dumbledore>}
        """
        if name not in self.nodes:
            self.nodes[name] = PersonNode(name)

    def set_friends(self, name, friend_names):
        """Set two people as friends.

        This is reciprocal, so if Romeo is friends with Juliet, she's friends with Romeo (graph is undirected)

        >>> f = FriendGraph()
        >>> f.add_person('Romeo')
        >>> f.add_person('Juliet')
        >>> f.set_friends('Romeo', ['Juliet'])

        >>> f.nodes['Romeo'].adjacent
        set([<PersonNode Juliet>])

        >>> f.nodes['Juliet'].adjacent
        set([<PersonNode Romeo>])
        """

        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    def are_connected(self, name1, name2):
        """Is this name1 friends with name2?"""

        if name1 is None or name2 is None:
            return False

        if name1.name == name2.name:
            return True

        while name1:
            for adj in self.nodes[name1]:
                self.are_connected(adj)

        return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"

