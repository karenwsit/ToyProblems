#http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/

#Runtime: O(n)
#Space: O(n)

def reverse_string_special(string):
    """
    >>> reverse_string_special('a,b$c')
    'c,b$a'
    >>> reverse_string_special("Ab,c,de!$")
    'ed,c,bA!$'
    """
    input_array = list(string)

    char_array = [',', '$', '!']
    temp_array = []

    for i in range(len(input_array)):
        if string[i] not in char_array:  # a special character
            temp_array.append(input_array[i])

    temp_array = temp_array[::-1]

    for i in range(len(input_array)):
        if input_array[i] not in char_array:
            new_element = temp_array.pop(0)
            input_array[i] = new_element

    return "".join(input_array)

#Will refactor to include more efficient solution of runtime O(n) and no extra space


if __name__ == '__main__':
    import doctest
    doctest.testmod()
