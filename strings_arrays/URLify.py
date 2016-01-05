#Exercise 1.3 of Cracking the Coding Interview
#Replace all spaces in a string with %20
#################################################################################

#Time: O(n)
#Space: O(n)

#Strings are immutable therefore a new string was created

def URLify(string):
    """
    >>> URLify('Mr John Smith')
    'Mr%20John%20Smith'
    """
    new_string = ""
    for char in string:
        if char == " ":
            new_string += "%20"
        else:
            new_string += char

    return new_string


# #################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
