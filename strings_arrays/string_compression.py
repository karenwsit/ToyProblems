#Exercise 1.6 of Cracking the Coding Interview
#Given a string, perform basic string compression using the counts of repeated characters.
#################################################################################

#Time: O(p + k^2) k = # of sequences (4 in this example) String concatenation operations O(n^2)
#The other alternative is to use a string builder - a resizable array of all strings.
#Space: O(n)

def compress(string):
    """
    >>> compress('aabcccccaaa')
    'a2b1c5a3'
    """

    compressed_string = ""
    count = 0

    for i in range(len(string)):
        count += 1
        if i+1 > (len(string) - 1) or string[i] != string[i+1]:
            compressed_string += "%s%d" % (string[i], count)
            count = 0
    if len(compressed_string) >= len(string):
        return string
    return compressed_string


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
