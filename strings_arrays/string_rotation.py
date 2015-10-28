#Exercise 1.9 of Cracking the Coding Interview
#Write a method that checks if one word is a substring of another. Given two strings, s1 & s2, write code to check if s2 is a rotation of s1 using only one call.
#################################################################################

def is_rotation(s1, s2):
    """
    >>> is_rotation('erbottlewat', 'waterbottle')
    True
    >>> is_rotation('something', 'something')
    True
    >>> is_rotation('dog', 'pig')
    False 
    """

    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1 == s2:
            return True
        s2 = s2[1:] + s2[0]
    return False

#Using isSubstring from CTCI

def is_rotation2(s1,s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
