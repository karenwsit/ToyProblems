"""
Find all permutations of an array of elements
http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
l = starting index
r = ending index
"""
#Runtime: O(n*n!)
#Solution will printe duplicate permutations if there are repeating characters
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

#This solution saves the results in a list
def permute2(s):
    """
    >>> permute2('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    res = []
    if len(s) == 1:
        res = [s]

    for i, c in enumerate(s):
        for perm in permute2(s[:i] + s[i+1:]):
            res += [c+perm]

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()