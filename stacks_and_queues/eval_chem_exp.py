"""
Infix to Postfix Evaluation
Count number of particles in a chemistry expression
Input: '((H2O)300(AM4B)6)2000'
'( ( H2O ) 300 ( AM4B ) 6 ) 2000'
Output: 1,872,000
"""

def infix(expr):
    input_list = expr.split() 
    #['(', '(', 'H2O', ')', '300', '(', 'AM4B', ')', '6', ')', '2000']

    output_list = []
    i = 0
    while i < len(input_list):
        if input_list[i] == ")":
            output_list.append(input_list[i])
            output_list.append("*")
        elif input_list[i] == "(" and input_list[i-1] != "(" and i != 0:
            output_list.append("+")
            output_list.append(input_list[i])
        else:
            output_list.append(input_list[i])
        i += 1
    return output_list
    #['(', '(', 'H2O', ')', '*', '300', '+', '(', 'AM4B', ')', '*', '6', ')', '*', '2000']


infix('( ( H2O ) 300 ( AM4B ) 6 ) 2000')
