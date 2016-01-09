def dec2bin(num):
    """Convert a decimal number to binary representation.

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'
    """

    binary_string = ""

    num_bit = 1

    while 2**num_bit < num:
        num_bit += 1

    for i in range(num_bit, -1, -1):
        if num - (2**i) >= 0:
            num -= (2**i)
            print "NUM: %d" % num
            binary_string += "1"
        else:
            binary_string += "0"
            
        print "STRING: %s" % binary_string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! \n"
