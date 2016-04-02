"""
Find the longest common substring
http://www.geeksforgeeks.org/longest-common-substring/
"""

def len_longest_substring(str1, str2):
    """
    >>> len_longest_substring('GeeksforGeeks', 'GeeksNow')
    5
    >>> len_longest_substring('puddingnana', 'Banana')
    4
    >>> len_longest_substring('academy', 'abracadabra')
    4
    """

    str1_list = list(str1)
    str2_list = list(str2)

    substring_dict = {}
    substring = ""

    if len(str1_list) > len(str2_list):
        short_list = str2_list
        long_list = str1_list
    else:
        short_list = str1_list
        long_list = str2_list

    for i in range(len(short_list)):
        for j in range(len(long_list)):
            if short_list[i] == long_list[j]:
                substring += short_list[i]
                break

    print substring

len_longest_substring('Banana', 'puddingnana')
