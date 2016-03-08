# Insertion Sort
# Runtime: O(n^2)
# Space: O(1)


def insertion_sort(alist):
    
    for index in range(1, len(alist)):
        currentval = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentval:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position]=currentval

    return alist
