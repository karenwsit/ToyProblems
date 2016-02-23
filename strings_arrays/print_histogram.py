#Print histogram horizontally & vertically

# "test me there"

# ****
# **
# *****

#   *
# * *
# * *
# ***
# ***

def print_histogram_reg(string):
    """
    """

    string_list = string.split()
    for word in string_list:
        print len(word) * '*'

# print_histogram_reg('test me here')

def print_histogram_ver(string):
    """
    """
    string_list = string.split()
    # print string_list
    max_length = len(max(string_list, key=len))  # row num

    new_string_list = []

    for word in string_list:
        new_string_list.append(len(word) * '*' + (max_length-len(word)) * '+')

    for j in range(max_length-1, 0, -1):
        for i in range(len(string_list)):
            print new_string_list[i][j]

    # Need to print new lines correctly; will refactor later

print_histogram_ver('test me there')
