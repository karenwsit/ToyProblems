#Exercise 1.9 of Cracking the Coding Interview
#Write a method that checks if one word is a substring of another. Given two strings, s1 & s2, write code to check if s2 is a rotation of s1 using only one call.
#################################################################################

def is_Substring(s1, s2):
    """
    >>> is_Substring('erbottlewat', 'waterbottle')
    True
    """

    if len(s1) != len(s2):
        return False
    for i in range(len(s2)):
        if s2[i] == s1[-1] and s2[i+1] == s1[0]:
            a = i+1
    subset1 = s2[:a]
    subset2 = s2[a:]

    new_string = "%s%s" % (subset2, subset1)

    if new_string == s1:
        return True
    return False


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
