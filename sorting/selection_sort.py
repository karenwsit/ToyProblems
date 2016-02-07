#Selection Sort:
def selection_sort(unsorted_array):
    """
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 25, 64]
    """
    sorted_array = []

    for i in range(len(unsorted_array)+1):
        minimum = unsorted_array[i]
        if unsorted_array[i+1] < minimum:
            minimum = unsorted_array[i+1]
        sorted_array.append(minimum)
    return sorted_array



if __name__ == "__main__":
    import doctest
    doctest.testmod()