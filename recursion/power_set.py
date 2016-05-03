"""
Find all permutations of a string
Input: string
Output: array of strings
"""

def powerSet(string):
    """
    >>> powerSet('abc')
    ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
    >>> powerSet('')
    ['']
    >>> powerSet('a')
    ['', 'a']
    >>> powerSet('ab')
    ['', 'a', 'b', 'ab']
    """
    if len(string) == 0:
        return [""]
    else:
        all_subsets = []
        for subset in powerSet(string[1:]):
            all_subsets.append(subset)
            new = string[0] + subset
            all_subsets.append(new)
        return all_subsets

def powerSet2(string):
    """
    >>> powerSet2('abc')
    ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
    >>> powerSet2('')
    ['']
    >>> powerSet2('a')
    ['', 'a']
    >>> powerSet2('ab')
    ['', 'b', 'a', 'ab']
    """
    result = []
    perm_dict = {}

    def traverse(buildUp, depth):
        if depth == len(string):
            key = "".join(sorted(buildUp))
            if key not in perm_dict:
                result.append(key)
                perm_dict[key] = True
            return
        else:
            #traverse left
            traverse(buildUp, depth+1)
            #traverse right
            traverse(buildUp + string[depth], depth+1)

    traverse("", 0)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()