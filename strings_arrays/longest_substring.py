"""
Find the longest common substring
http://www.geeksforgeeks.org/longest-common-substring/
"""

#Runtime: O(m^2 * n)

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

#Runtime: O(mn)
#Space: O(mn)

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
    print lcs_set

#Runtime: O(mn)
#Space: O(mn)

def lcs2(s1, s2):
    m = len(s1)
    n = len(s2)
    count_mat = [[0] * (n+1) for i in xrange(m+1)]
    longest, x_longest = 0, 0
    for i in xrange(1, 1 + m):
        for j in xrange(1, 1 + n):
            if s1[i - 1] == s2[j - 1]:
                count_mat[i][j] = count_mat[i - 1][j - 1] + 1
                if count_mat[i][j] > longest:
                    longest = count_mat[i][j]
                    x_longest = i
            else:
                count_mat[i][j] = 0
    print s1[x_longest - longest: x_longest]

lcs2('GeeksforGeeks', 'GeeksNow')
lcs2('Banana', 'puddingnana')
lcs2('academy', 'abracadabra')
