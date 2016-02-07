#Binary Search: Return its location
#Runtime: O(n)

def binary_search(sorted_array, x):

    for i in range(len(sorted_array)):
        if sorted_array[i] == x:
            return i
    return -1


