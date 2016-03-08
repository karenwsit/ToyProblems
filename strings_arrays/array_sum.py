#Write a function that takes an array of unsorted integers & a sum.
#Returns a boolean if 2 integers within the array sum to the given sum


def array_sum(arr, summ):
    """
    >>> array_sum([1, 5, 3], 8)
    True
    >>> array_sum([1, 5, 3], 9)
    False
    """
    #sort an array O(nlogn)
    sorted_array = sorted(arr)

    for i in range(len(arr)):
        remain = summ - sorted_array[i]
        if binary_search(sorted_array, remain):
            return True
    return False

#RunTime: O(logn)
def binary_search(sorted_array, remain):
    """
    >>> binary_search([1, 3, 5], 3)
    True
    >>> binary_search([1, 3, 5], 4)
    False
    """
    if len(sorted_array) == 0:
        return False
    else:
        mid_point = len(sorted_array)//2
        if sorted_array[mid_point] == remain:
            return True
        elif remain < sorted_array[mid_point]:
            lower = sorted_array[:mid_point]
            return binary_search(lower, remain)
        else:
            upper = sorted_array[mid_point+1:]
            return binary_search(upper, remain)


if __name__ == '__main__':
    import doctest
    doctest.testmod()