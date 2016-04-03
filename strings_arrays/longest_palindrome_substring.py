"""
Find the longest palindromic substring
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
"""

def flp(string):
    """
    >>> flp('bananas')
    'anana'
    >>> flp('tacocat')
    'tacocat'
    >>> flp('almond')
    False
    """
    results = []
    for i in range(len(string)):
        for j in range(i,len(string)+1):
            if is_palindrome(string[i:j]):
                results.append(string[i:j])

    if not results:
        return False

    new_results = sorted(results, key=len)  #creates a new list; in place sorting will be results.sort(key=len)
    if new_results:
        return new_results[-1]

def is_palindrome(string):
    if len(string) > 2:
        return string == string[::-1]
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
