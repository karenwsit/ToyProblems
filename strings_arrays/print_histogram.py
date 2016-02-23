#Print histogram horizontally & vertically

# "test me there"

#****
#**
#*****

#   *
# * *
# * *
# ***
# ***


def print_histogram_reg(string):
    string_list = string.split()
    for word in string_list:
        print len(word) * '*'

# print_histogram_reg('test me here')