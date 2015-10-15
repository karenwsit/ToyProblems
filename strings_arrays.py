####### EX. 1.1 ########

def is_unique_string(word):
    uchars = set()
    for c in word:
        if c in uchars:
            print False
        else:
            uchars.add(c)
    return True

# is_unique_string('tornado')

####### EX. 1.2 ########

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    if sorted(str1) == sorted(str2):
        print True
    else:
        print False

# check_permutation("god", "Dog")

####### EX. 1.3 ########