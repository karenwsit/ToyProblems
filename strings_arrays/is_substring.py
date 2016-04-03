#http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
#################################################################################

def is_substring(long_string, substring, i=0, index_array=None):
    """
    >>> is_substring('AABAABACAADAABA', 'AABA')
    [0, 3, 11]
    >>> is_substring('A', 'AABA')
    False
    """
    if index_array is None:
        index_array = []
    if len(long_string) < len(substring):
        return False

    if i > len(long_string) - len(substring):
        return index_array

    check_string = ""

    for j in range(i, i + len(substring)):
        check_string += long_string[j]

    if check_string == substring:
        index_array.append(i)

    return is_substring(long_string, substring, i+1, index_array)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
