#Exercise 1.4 of Cracking the Coding Interview
#Given a string, write a function to check if it is a permutation of a palindrome
#################################################################################

#Time: O(n)
#Space: O(n)

def is_palindrome(string):
    """
    >>> is_palindrome('atco cta')
    True
    """
    new_string = string.lower()
    odd_list = []
    for char in new_string:
        if char == " ":
            continue
        if new_string.count(char) % 2 != 0:
            odd_list.append(char)
    if len(odd_list) != 1:
        return False
    return True

#Time: O(n)
#Space: O(n)

def is_palindrome2(string):
    """
    >>> is_palindrome2('Taco Cat')
    True
    >>> is_palindrome2('cheesepie YUM')
    False
    """
    new_string = string.lower()
    frequency_dict = {}
    for char in new_string:
        if char == ' ':
            continue
        frequency_dict[char] = frequency_dict.get(char,0) + 1

    odd_list = [char for char, count in frequency_dict.iteritems() if count %2 != 0]
    if len(odd_list) > 1:
        return False
    return True


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
