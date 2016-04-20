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

def postfix(expr2):
    print expr2
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    op_stack = []
    postfix_list = []
    for token in expr2:
        if token not in prec and token != ')':
            postfix_list.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while len(op_stack) != 0 and (prec[op_stack[-1]] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.append(token)

    while len(op_stack) != 0:
        postfix_list.append(op_stack.pop())

    return postfix_list  #['H2O', '300', '*', 'AM4B', '6', '*', '+', '2000', '*']


def eval(expr3):
 

expr2 = infix('( ( H2O ) 300 ( AM4B ) 6 ) 2000')
postfix(expr2)