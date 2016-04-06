"""
Breadth First Search Implementation
"""
graph = {'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']}

def bfs(graph, start, end):
    #queue of paths
    queue = []
    #push the first path into the queue
    queue.append([start])

    while queue:
        path = queue.pop(0)  # get first path from the queue
        node = path[-1]  # get last node from path
        if node == end:  # path found
            return path
        #enumerate all adjacent nodes; construct new path & push into queue
        for adj_node in graph.get(node,[]):
            new_path = list(path)
            new_path.append(adj_node)
            queue.append(new_path)

