"""
http://www.geeksforgeeks.org/find-excel-column-name-given-number/
Given an integer, return the string column header for that indexed column in excel.
1:A, 26:Z, 27:AA, 28:AB, 52:AZ, 53:BA, 702:ZZ, 703:AAA
"""

def excel(integer):
    """
    >>> excel(26)
    'Z'
    >>> excel(51)
    'AY'
    >>> excel(52)
    'AZ'
    >>> excel(676)
    'YZ'
    >>> excel(702)
    'ZZ'
    >>> excel(705)
    'AAC'
    """
    res = ""
    n = integer
    int_dict = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z'
    }
    while n > 0:
        remain = n%26
        if remain == 0:
            res += 'Z'
            n = (n/26)-1
        else:
            res += int_dict[remain]
            n = n/26
    return res[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

