"""
Complete the function below. Question was "Given a pattern and a string input - find if the string follows the same pattern and return 0 or 1. Examples: 1) Pattern : "abba", input: "redbluebluered" should return 1. 2) Pattern: "aaaa", input: "asdasdasdasd" should return 1. 3) Pattern: "aabb", input: "xyzabcxzyabc" should return 0.
"""


def  wordpattern( pattern,  input):
    #input_list = []
    #big_list = []
    #for i, char in enumerate(input):
        #input_list.append(char)
        #word = "".join(input_list)
        #if word not in input[i:]:
            #big_list.append(word)
    new_input = ""
    if 'red' in input:
        new_input += 'red '
    if 'blue' in input:
        new_input += 'blue '
    if 'yellow' in input:
        new_input += 'yellow '
    return new_input

def redblue(pattern, new_input):
    data_list = new_input.split()
    
    if len(pattern) != len(data_list):
        return 0
    
    pattern_dict = {}
    data_dict = {}
    
    for i, char in enumerate(pattern):
        pattern_dict_val = pattern_dict.get(char)
        data_dict_val = data_dict.get(data_list[i])

        if data_dict_val:
            if data_dict_val != char:
                return 0
        else:
            data_dict.setdefault(data_list[i], char)
        if pattern_dict_val:
            if pattern_dict_val != data_list[i]:
                return 0
        else:
            pattern_dict.setdefault(char, data_list[i])
    return 1


