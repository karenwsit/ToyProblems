"""
input: string
output: array of strings

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()