#Willson's rockpaperscissors problem
# Write a function that generates every sequence of throws a single player could throw over a three-round game of rock-paper-scissors
#################################################################################

def find_combos(n):
    """
    >>> find_combos(2)
    [['r', 'r'], ['r', 'p'], ['r', 's'], ['p', 'r'], ['p', 'p'], ['p', 's'], ['s', 'r'], ['s', 'p'], ['s', 's']]
    """
    if n <= 0 :
        return []
    if n == 1:
        return [['r'], ['p'], ['s']]
    else:
        result = []
        previous = find_combos(n-1)
        for each in previous:
            for new_array in transform(each):
                result.append(new_array)
    return result

def transform(array):
    choices = ['r', 'p', 's']
    new_array = []
    for choice in choices:
        inner_array = []
        inner_array.append(array[0])
        inner_array.append(choice)
        new_array.append(inner_array)
    return new_array

#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
