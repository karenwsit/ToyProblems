"""Given a word list, find the word with the most anagrams in the list."""

def make_anagram_dict(words):
    """Return dictionary mapping sorted letters -> [words with the letters]

        >>> make_anagram_dict(["act", "cat", "dog", "mouse", "god"])
        {'emosu': ['mouse'], 'dgo': ['dog', 'god'], 'act': ['act', 'cat']}
    """
    anagram_dict = {}

    for word in words:
        for key, value in anagram_dict.iteritems():
            if sorted(key) == sorted(word):
                anagram_dict[key] 
    

def find_most_anagrams_from_wordlist(wordlist):
    """Given a list of words, return the word with the most anagrams.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """

    for word in wordlist:
        make_anagram_dict(word)





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"