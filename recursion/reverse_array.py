#Willson's reverse an array recursion problem
#Write a solution twice (non-recursively &recursively) that returns a reversed array
#################################################################################

def reverse(array):
    """
    >>> reverse([])
    []
    >>> reverse([1])
    [1]
    >>> reverse([1,2])
    [2, 1]
    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    result_array = []
    if len(array) == 1:
        return array
    while len(array) > 0:
        result_array.append(array.pop())

    return result_array


def recursive_reverse(array):
    """
    >>> reverse([])
    []
    >>> reverse([1])
    [1]
    >>> reverse([1,2])
    [2, 1]
    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    if len(array) <= 1:
        return array
    else:
        pop_int = array.pop(0)
        result_array = recursive_reverse(array)
        result_array.append(pop_int)
        return result_array


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
