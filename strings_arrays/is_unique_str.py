#Exercise 1.1 of Cracking the Coding Interview               
#Implement an algorithm to determine if a string has all unique characters   
#################################################################################

# Time: O(n)
# Space: O(n)

def is_unique(string):
    """ 
    >>> is_unique("tornado")
    False
    >>> is_unique("python")
    True
    """

    unique_chars = set()

    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

#Implement an algorithm to determine if a string has all unique characters without other data structures

# Time: O(n)
# Space: O(n)

def is_unique2(string):
    """
    >>> is_unique2("academy")
    False
    >>> is_unique2("pickle")
    True
    """
    for c in string:
        if string.count(c) > 1:
            return False
    else:
        return True

#Time: O(n log(n))
#Space: O(n)

def is_unique3(string):
    """
    >>> is_unique2("university")
    False
    >>> is_unique2("towel")
    True
    """
    sorted_string = sorted(string)
    for i in range(len(string)-1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True

#Time: O(n^2)
#Space: O(1)

def is_unique4(string):
    """
    >>> is_unique2("university")
    False
    >>> is_unique2("towel")
    True
    """
    for i, char in enumerate(string):
        for j, char2 in enumerate(string):
            if char == char2 and i != j:
                return False
    return True


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
