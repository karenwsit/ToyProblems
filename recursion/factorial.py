#Willson's factorial recursion problem
#Write a solution twice (non-recursively &recursively) that returns the factorial of any integer 
#################################################################################

def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(11)
    39916800
    """
    prod = 1
    for int in range(1, n+1):
        prod *= int
    return prod


def recursive_factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(11)
    39916800
    """
    if n == 0:
        return 1
    else:
        product = n * recursive_factorial(n-1)
    return product


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
