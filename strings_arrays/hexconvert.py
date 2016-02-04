def hex_convert(hex_in):
    """Convert a hexidecimal string, like '1A', into it's decimal equivalent.

        >>> hex_convert('6')
        6

        >>> hex_convert('10')
        16

        >>> hex_convert('FF')
        255

        >>> hex_convert('FFFF')
        65535
"""

    hex_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    result = 0

    for i, hex_char in enumerate(hex_in[::-1]):
        result += (hex_dict[hex_char] * (16**i))

    return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS.\n"
