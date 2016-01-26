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


#Simple graph traversal, check to see if node is found using Queue (list of lists)
#Graph is in an adjacent list representation

graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

def bfs(graph, start, end):
    queue = []

    queue.append([start])   # push 1st path into queue

    while queue:
        path = queue.pop(0)
        node = path[-1]  # get last node from path
        if node == end:
            return path

        for adjacent in graph.get(node,[]):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

    return None


#CTCI solution: Simple graph traversal, check to see if node is found & keep track of visited nodes"
#Iterative Implementation of Breadth-First Search using deque

class DirectedGraph:
    def __init__(self, content):
        self.content = content
        self.neighbors = []

def find_path2(start, end):
    if start is end:
        return True
    elif start is None or end is None:
        return False

    visited = set([start, end])

    from Queue import deque  # double-ended queue supports adding & removing elements from either end
    queue = deque([start])

    while len(queue) > 0:
        node = queue.popleft()
        for child in node.neighbors:
            if child is end:
                return True
            elif child not in visited:
                visited.add(child)
                queue.append(child)
    return False


#For a non-directed graph, iterative implemention of Breadth-First Search - Non-recursive
def find_path3(start, end):
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
