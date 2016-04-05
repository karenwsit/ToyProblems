#Binary Search
#Runtime: O(logn)

def binary_search(sorted_array, x):
    """
    >>> binary_search([1,2,3,4,5], 1)
    True
    >>> binary_search([1,2,3,4,5], 6)
    False
    """
    if sorted_array == []:
        return False
    mid = len(sorted_array) // 2
    if x == sorted_array[mid]:
        return True
    elif x < sorted_array[mid]:
        return binary_search(sorted_array[:mid], x)
    elif x > sorted_array[mid]:
        return binary_search(sorted_array[mid+1:], x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()