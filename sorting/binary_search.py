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
    else:
        mid = len(sorted_array) // 2
        if x == sorted_array[mid]:
            return True
        elif x < sorted_array[mid]:
            return binary_search(sorted_array[:mid], x)
        elif x > sorted_array[mid]:
            return binary_search(sorted_array[mid+1:], x)

#Non-recursive solution
# Find and return the index of key in sequence sorted_array; -1 if not found
def search_binary(sorted_array, x):
    """
    >>> search_binary([1,2,3,4,5], 1)
    0
    >>> search_binary([1,2,3,4,5], 4)
    3
    >>> search_binary([1,2,3], 4)
    -1
    """
    lb = 0
    ub = len(sorted_array)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = sorted_array[mid_index]

        # How does the probed item compare to the x?
        if item_at_mid == x:
            return mid_index      # Found it!
        if item_at_mid < x:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

if __name__ == "__main__":
    import doctest
    doctest.testmod()