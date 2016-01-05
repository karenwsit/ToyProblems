"""Given a word list, find the word with the most anagrams in the list."""

def make_anagram_dict(words):
    """Return dictionary mapping sorted letters -> [words with the letters]

        >>> make_anagram_dict(["act", "cat", "dog", "mouse", "god"])
        {'emosu': ['mouse'], 'dgo': ['dog', 'god'], 'act': ['act', 'cat']}
    """
    anagram_dict = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_dict.setdefault(sorted_word, []).append(word)

    return anagram_dict

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

    full_anagram_dict = make_anagram_dict(wordlist)

    #two tracker variables that will be updated as we iterate through the wordlist
    highest_num_anagrams = 0
    most_anagrams_word = None

    for word in wordlist:
        sorted_word = "".join(sorted(word))
        number_anagrams = len(full_anagram_dict[sorted_word])
        if number_anagrams > highest_num_anagrams:
            highest_num_anagrams = number_anagrams
            most_anagrams_word = word

    return most_anagrams_word


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"