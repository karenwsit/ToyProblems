#Quick Sort - sorting done in place
#Runtime: O(n^2)
#Space: O(log(n))


def quick_sort(lst):

    """
    >>> quick_sort([1, 6, 0, 3, 5, 4, -20, 7])
    [-20, 0, 1, 3, 4, 5, 6, 7]
    >>> quick_sort([4, 8, 3, 1, 5])
    [1, 3, 4, 5, 8]
    """
    quick_sort_helper(lst, 0, len(lst)-1)
    return lst

def quick_sort_helper(lst, start, end):
    if start < end:
        #base case where if the list provided <= len 1, it is already sorted
        split_point = partition(lst, start, end)

        quick_sort_helper(lst, start, split_point-1)  #left side of split_point
        quick_sort_helper(lst, split_point+1, end)  #right side of split_point


def partition(lst, start, end):

    pivot = lst[start]
    left = start + 1
    right = end

    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left = left + 1

        while lst[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp

    temp = lst[start]
    lst[start] = lst[right]
    lst[right] = temp

    return right

if __name__ == '__main__':
    import doctest
    doctest.testmod()
