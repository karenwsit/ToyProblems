"""
Variation of CTCI 4.1: (Find out whether or not there is a route between 2 nodes)
Find the shortest path between 2 nodes
"""

def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []

    path += [start]

    if start == end:
        return path

    if start not in graph:
        return []

    all_paths = []

    for node in graph[start]:
        if node not in path:
            new_paths = find_shortest_path(graph, node, end, path)
            for new_path in new_paths:
                all_paths.append(new_path)

    return all_paths

def find_shortest_path(all_paths):

    sorted_paths = sorted(all_paths)
    return sorted_paths[0]

def main():
    find_shortest_path(find_all_paths())


"""
Alternate solution without sorting
"""

def find_shortest_path2(graph, start, end, path=None):
    if path is None:
        path = []
         
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path2(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest
