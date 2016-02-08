#Selection Sort:
def selection_sort(an_array):
    """
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """

    for i in range(len(an_array)):
        min_index = i
        for j in range(i+1,len(an_array)):
            if an_array[j] < an_array[min_index]:
                min_index = j
        temp = an_array[i]
        an_array[i] = an_array[min_index]
        an_array[min_index] = temp
    return an_array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
