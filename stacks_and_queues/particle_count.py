"""
Return number of particles given a chemistry expression
"""
import re

def count_particles(string):
    alist = re.split(r'\(|\)', string) #['', '', 'H2O', '300', 'AM4B', '6', '2000']

    new_list = []

    for element in alist:
        if element == "":
            continue
        elif element.isdigit():
            new_list.append(int(element))
        else:
            new_list.append(element)
    
    # ['H2O', 300, 'AM4B', 6, 2000]

    count = 0

    for element in new_list:
        if isinstance(element, str):
            for char in element:
                if char.isdigit():

            count
    # string_list = string.split()
    # print string_list
    # stack = []
    # count = 0
    # for char in string:
    #     if char == '(':
    #         stack.append(char)
    #     if char == ')':
    #         stack.pop(-1)
    #     if char.isalpha():
    #         count += 1
    #     if char.isdigit():
    #         if count != 1:
    #             count -= 1
    #         count * int(char)

    # return count

count_particles(r'((H2O)300(AM4B)6)2000')

# ( (H2O)300)

# [H20, 300, AM4B, 6, 2000]
