#Exercise 4.1 of Cracking the Coding Interview
#Given a directed graph, design an algorithm to find out whether there is a path route between two nodes
#################################################################################

#Recursive Solution
def find_path(graph, start, end, path=[]):
    path += [start]

    #this is the base case:
    if start == end:
        return path

    if start not in graph:
        return None

    for adj_node in graph[start]:
        if adj_node not in path:
            new_path = find_path(graph, adj_node, end, path)
            if new_path:
                return new_path

    return None

#For a non-directed graph
#Breadth-First Search - Not recursive

def find_path2(start, end):
    possible_nodes = Queue()
    seen = set()

    possible_nodes.enqueue(start)
    seen.add(start)

    while not possible_nodes.is_empty():
        start = possible_nodes.dequeue()

        if start == end:
            return True
        else:
            for adj_node in start.adjacent:
                if adj_node not in seen:
                    possible_nodes.enqueue(adj_node)
                    seen.add(adj_node)
    return None



#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
