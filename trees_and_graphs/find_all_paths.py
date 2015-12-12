"""
Variation of CTCI 4.1: Find out whether or not there is a route between 2 nodes
"""

def find_all_paths(graph, start, end, path=[]):
    path += [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    all_paths = []

    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)

            for new_path in new_paths:
                all_paths.append(new_path)

    return all_paths




