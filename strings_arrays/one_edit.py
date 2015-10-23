#Exercise 1.5 of Cracking the Coding Interview
#Given 2 strings, write a function to check if they are one edit away (or zero edits).
#################################################################################

#Time: O(n) where n = length of the shorter string
#Space: O(n)

# def one_edit_away(str1, str2):
#     """
#     >>> one_edit_away('pale','ple')
#     True
#     >>> one_edit_away('pales','pale')
#     True
#     >>> one_edit_away('pale', 'bale')
#     True
#     >>> one_edit_away('pale', 'bake')
#     False
#     """
#     if len(str1) > (len(str2) + 1) or len(str1) < (len(str2) - 1):
#         return False
#     if len(str2) > (len(str1) + 1) or len(str2) < (len(str1) - 1):
#         return False
#     if len(str1) == len(str2):
#         count = 0
#         for i in range(len(str1)-1):
#             if str1[i] != str2[i]:
#                 count += 1
#                 if count > 1:
#                     return False
#     return True


def one_edit_away(str1, str2):
    """
    >>> one_edit_away('pale','ple')
    True
    >>> one_edit_away('pales','pale')
    True
    >>> one_edit_away('pale', 'bale')
    True
    >>> one_edit_away('pale', 'bake')
    False
    """
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    if len(str1) + 1 == len(str2):
        return one_edit_insert(str1, str2)
    if len(str1) - 1 == len(str2):
        return one_edit_insert(str2, str1)
    return False

def one_edit_replace(str1, str2):
    found_difference = False
    for i in range(len(str1)-1):
        if str1[i] != str2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

        # count = 0
        # for i in range(len(str1)-1):
        #     if str1[i] != str2[i]:
        #         count += 1
        #         if count > 1:
        #             return False
    # return True

def one_edit_insert(str1, str2):
    index1 = 0
    index2 = 0
    while (index2 < len(str2)) and (index1 < len(str1)):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
