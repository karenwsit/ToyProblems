"""
Find Excel column name from a given column number
http://www.geeksforgeeks.org/find-excel-column-name-given-number/
"""

"""
Given an integer, return the string column header for that indexed column in excel.

Examples you write on the board:
1 -> ‘A’, 26 -> ‘Z’, 27 -> ‘AA’, 28 --> 'AB', 52 -> ‘AZ’, 53 -> ‘BA’, …702 -->'ZZ' --> 703 -->'AAA'
27-52 --> 'A'
53-79 --> 'B'
"""

def excel(integer):
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

excel(80)