#http://www.geeksforgeeks.org/reverse-words-in-a-given-string/
#################################################################################

def reverse_words(string):
    """
    >>> reverse_words("i like this program very much.")
    'much. very program this like i'
    >>> reverse_words("Karen's a great coder")
    "coder great a Karen's"
    """

    sent_array = []
    sent_array = string.split()
    sent_array = sent_array[::-1]
    reversed_string = " ".join(sent_array)
    return reversed_string


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

