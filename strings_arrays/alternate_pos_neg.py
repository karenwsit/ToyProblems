def alternate_pos_neg(num_list):
    """
    Given a list of numbers, returns a list with alternating positive and negative 
    numbers while maintaining order. If there are more positive numbers than negative
    numbers, they appear at the end of the array, and vice versa.

    >>> alternate_pos_neg([1, 2, 3, -4, -1, 4])
    [1, -4, 2, -1, 3, 4]
    >>> alternate_pos_neg([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
    [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
    >>> alternate_pos_neg([-1, -2, 3, -4])
    [3, -1, -2, -4]
    """

    pos_array = []
    neg_array = []
    result_array = []

    for num in num_list:
        if num < 0:
            neg_array.append(num)
        else:
            pos_array.append(num)

    i = 0
    j = 0

    while i < len(pos_array) or j < len(neg_array):
        if i < len(pos_array):
            result_array.append(pos_array[i])
        if j < len(neg_array):
            result_array.append(neg_array[j])
        i += 1
        j += 1

    # while len(pos_array) > 0 or len(neg_array) > 0:
    #     if pos_array == []:
    #         result_array.append(neg_array.pop(0))
    #     elif neg_array == []:
    #         result_array.append(pos_array.pop(0))
    #     else:
    #         result_array.append(pos_array.pop(0))
    #         result_array.append(neg_array.pop(0))

    # return result_array
    
########################################################################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()
