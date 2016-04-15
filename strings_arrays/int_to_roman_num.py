"""Write function takes in integer and outputs roman numerals string

1: 'I'
2: 'II'
3: 'III'
4: 'IV'
5: 'V'
6: 'VI'
7: 'VII'
8: 'VIII'
    9: 'IX'
10: 'X'
12: 'XII'
15: 'XV'
20: 'XX'
30: 'XXX'
    40: 'XL'
50: 'L'
    90: 'XC'
    96: 'XCVI'
100: 'C'
500: 'D'
1000: 'M'
No more than 3 of same letters in a row; exception for 'M'
"""
def roman_num(num):
    """
    >>> roman_num(2002)
    'MMII'
    >>> roman_num(1999)
    'MCMXCIX'
    >>> roman_num(96)
    'XCVI'
    """
    res = ""
    n = num
    roman_dict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    if n in roman_dict:
        return roman_dict[n]
    else:
        while n > 0:
            for key in sorted(roman_dict.iterkeys(), reverse=True):
                if key <= n:
                    res += roman_dict[key]
                    n = n - key
                    break

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
    ones_place = num%10 #0
    tens_place = (num / 10) %10 #8
    hun_place = (num / 100) %10 #2
    tho_place = (num / 1000) %10 #5

    res = tho_place*'M'
    
    if hun_place == 4:
        res += 'CD'
    elif hun_place >= 5:
        remain = hun_place - 5
        if remain == 4:
            res += 'CD'
        res += 'D'+ remain*'C'
    else:
        res += hun_place*'C'
    
    if tens_place == 4:
        res += 'XL'
    elif tens_place >= 5:
        remain = tens_place - 5
        if remain == 4:
            res += 'XL'
        else:
            res += 'L'+ remain*'X'
    else:
        res += tens_place*'X'

    if ones_place == 4:
        res += 'IV'
    elif ones_place >= 5:
        remain = ones_place - 5
        if remain == 4:
            res += 'IV'
        res += 'V'+ remain*'I'
    else:
        res += ones_place*'I'

    return res

print roman_num(5250)


Ex: 5280
'MMMMMCCLXXX'
5680
'MMMMMDCLXXX'
5240 --> 4
'MMMMMCCXL'
MMMMCCXXXX
5290 --> 4
want: MMMMMCCXC
current: MMMMMCCLXXXX
MMMMMCCL
"""



