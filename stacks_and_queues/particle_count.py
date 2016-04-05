"""
Return number of particles given a chemistry expression
"""
import re

#With Regex
def count_particles(string):
    alist = re.split(r'\(|\)', string) 
    #['', '', 'H2O', '300', 'AM4B', '6', '2000']

    new_list = []

    for element in alist:
        if element == "":
            continue
        elif element.isdigit():
            new_list.append(int(element))
        else:
            new_list.append(element)
    
    # Want:  ['H2O', 300, 'AM4B', 6, 2000]

#Without Regex
def count_particles(string):
    for element in new_list:
        if isinstance(element, string):
            for char in element:
                if char.isdigit():

    string_list = string.split()
    stack = []
    count = 0
    for char in string:
        if char == '(':
            stack.append(char)
        if char == ')':
            stack.pop(-1)
        if char.isalpha():
            count += 1
        if char.isdigit():
            if count != 1:
                count -= 1
            count * int(char)

    return count

count_particles(r'((H2O)300(AM4B)6)2000')

# ( (H2O)300)

# [H20, 300, AM4B, 6, 2000]
