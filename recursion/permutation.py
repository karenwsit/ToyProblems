"""
Find all permutations of an array of elements
http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""

def permute(a, l, r):
    """
    >>> permute(["J","O","N"], 0, 2)
    ['J', 'O', 'N']
    ['J', 'N', 'O']
    ['O', 'J', 'N']
    ['O', 'N', 'J']
    ['N', 'O', 'J']
    ['N', 'J', 'O']
    """
    if l==r:
        print a
    else:
        for i in xrange(l, r+1):
            a[l], a[i] = a[i], a[l] # swap
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

if __name__ == "__main__":
    import doctest
    doctest.testmod()