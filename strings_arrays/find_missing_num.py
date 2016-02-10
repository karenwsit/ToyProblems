#GeeksforGeeks: http://www.geeksforgeeks.org/find-the-missing-number/
"""
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in list. One of the integers is missing in the list.
Write an efficient code to find the missing integer.
"""


#RunTime: O(n)
def find_missing_num(num_array):
    """
    >>> find_missing_num([6, 3, 4, 1, 8, 7, 2])
    5
    """
    if num_array is None or len(num_array) < 1:
        return None
    n = len(num_array) + 1
    sum_of_series = ((n * (n+1) ) / 2)
    return sum_of_series - sum(num_array)



#RunTime: O(nlogn)
def find_missing_num2(num_array):
    """
    >>> find_missing_num2([6, 3, 4, 1, 8, 7, 2])
    5
    """
    sorted_array = sorted(num_array)
    for i in range(len(sorted_array)-1):
        if sorted_array[i+1] - sorted_array[i] != 1:
            return sorted_array[i] + 1

    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
