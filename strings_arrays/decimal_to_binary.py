def dec2bin(num):
    """Convert a decimal number to binary representation.

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(9)
    '1001'

    >>> dec2bin(15)
    '1111'
    """

    binary_string = ""

    num_bit = 1

    while 2 ** num_bit <= num:
        num_bit += 1
    print num_bit

    for i in range(num_bit-1, -1, -1):
        if (2**i) <= num:
            print "i", i
            print "2**i", 2**i
            num -= (2**i)
            binary_string += "1"
        else:
            binary_string += "0"

    return binary_string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! \n"
