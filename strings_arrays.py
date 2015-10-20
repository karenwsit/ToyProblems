####### EX. 1.3 ########

def replace_spaces(str):
    new_str = ""
    for char in str:
        if char == " ":
            new_str += "%20"
        else:
            new_str += char
    print new_str

# replace_spaces("Mr John Smith")

####### EX. 1.4 ########
