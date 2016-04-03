"""
Find the longest palindromic substring
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
"""

#Runtime: O(n^3)

def flp(string):
    """
    >>> flp('bananas')
    'anana'
    >>> flp('tacocat')
    'tacocat'
    >>> flp('almond')
    ''
    """
    results = []
    for i in range(len(string)):
        for j in range(i,len(string)+1):
            if is_palindrome(string[i:j]):
                results.append(string[i:j])

    if not results:
        return ''

    new_results = sorted(results, key=len)  #creates a new list; in place sorting will be results.sort(key=len)
    if new_results:
        return new_results[-1]

def is_palindrome(string):
    if len(string) > 2:
        return string == string[::-1]
    return False


#Dynamic Programming Solution
#Runtime: O(n^2)

def longestPalindrome(s):
    """
    >>> longestPalindrome('bananas')
    'anana'
    >>> longestPalindrome('tacocat')
    'tacocat'
    >>> longestPalindrome('almond')
    ''
    """
    n = len(s)
    t = [[False for i in range(n)] for j in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        t[i][i] = True
    for i in range(n - 1):
        j = i + 1
        if s[i] == s[j]:
            t[i][j] = True
            start = i
            max_len = 2
    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and t[i + 1][j - 1]:
                t[i][j] = True
                start = i
                max_len = l
    if len(s[start:start + max_len]) > 2:
        return s[start:start + max_len]
    else:
        return ''

#Dynamic Programming Solution; this only gives the length of the longest palindromic substring
#Runtime: O(n^2)

def flp2(string):
    """
    >>> flp2('bananas')
    5
    >>> flp2('tacocat')
    7
    >>> flp2('almond')
    1
    """
    n = len(string)
    C = [[0]*n for x in range(n)]

    #Strings of length 1 are palindrome of length 1
    for i in range(n):
        C[i][i] = 1

    #sl is length of substring
    for sl in range(2,n+1):
        for i in range(n-sl+1):
            j = i+sl-1
            if string[i] == string[j] and sl == 2:
                C[i][j] = 2
            elif string[i] == string[j]:
                C[i][j] = C[i+1][j-1] + 2
            else:
                C[i][j] = max(C[i][j-1], C[i+1][j])
    return C[0][n-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
