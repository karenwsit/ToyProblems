#Bubble Sort
#RunTime: O(n^2)

def bubble_sort(l):
    """
    >>> bubble_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """
    is_sorted = False

    while is_sorted is False:
        is_sorted = True

        for i in range(len(l)-1):
            num1, num2 = l[i], l[i+1]

            if num1 > num2:
                is_sorted = False
                l[i], l[i+1] = num2, num1

    return l


def bubble_sort2(an_array):
    """
    >>> bubble_sort2([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """

    for num in range(len(an_array)-1, 0, -1):
        for i in range(num):
            if an_array[i] > an_array[i+1]:
                temp = an_array[i]
                an_array[i] = an_array[i+1]
                an_array[i+1] = temp
    return an_array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
