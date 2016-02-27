#For a undirected graph with tree characteristics, we can choose any node as the root. 
#The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). 
#Given such a graph, write a function to find all the MHTs and return a list of their root labels.


def find_mht(n=None, edges=None):
    """
    >>> find_mht(n=4, edges=[[1, 0], [1, 2], [1, 3]])
    [1]
    >>> find_mht(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    [3, 4]
    """
    if n == 0:
        return [0]

    adj = [set() for _ in xrange(n)]

    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in xrange(n) if len(adj[i]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1:
                new_leaves.append(j)

    return leaves


find_mht(n=4, edges=[[1, 0], [1, 2], [1, 3]])

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()