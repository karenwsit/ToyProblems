#Exercise 1.2 of Cracking the Coding Interview
#Given 2 strings, write a method to decide if one is a permutation of the other
#################################################################################

#Time: O(n log(n))
#Space: O(n)

def check_permutation(str1, str2):
    """
    >>> check_permutation("god", "dog")
    True
    >>> check_permutation("dog", "cat")
    False
    """
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    return False

#Time: O(n)
#Space: O(n)

def check_permutation2(str1, str2):
    """
    >>> check_permutation("bfieowpadf", "fdapwoeifb")
    True
    >>> check_permutation("coding", "interview")
    False
    """
    dict_counts = {}
    dict_counts2 = {}
    for char1 in str1:
        dict_counts[char1] = str1.count(char1)
    for char2 in str2:
        dict_counts[char2] = str2.count(char1)

    if dict_counts[char2] == dict_counts[char1]:
        return True
    return False

#Time: O(n)
#Space: O(n)

def check_permutation3(str1, str2):
    """
    >>> check_permutation("bfieowpadf", "fdapwoeifb")
    True
    >>> check_permutation("coding", "interview")
    False
    """
    dict_counts = {}
    for char1 in str1:
        dict_counts[char1] = str1.count(char1)

    for char2 in str2:
        if char2 in dict_counts:
            dict_counts[char2] -= 1

    for char, count in dict_counts.iteritems():
        if count == 0:
            return True
    return False


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
