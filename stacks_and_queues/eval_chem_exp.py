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


def eval_str(expr3):
    output_list = []
    for element in expr3:
        if element == '*' or element == '+':
            output_list.append(element)
        elif element.isdigit() == True:
            output_list.append(int(element))
        else:
            total_num = 0
            char_num = 0
            for i in range(len(element)):
                if element[i].isdigit():
                    char_num += 1
                    total_num += int(element[i]) 
            output_list.append(len(element)-(char_num*2)+total_num)
    return output_list  #[3, 300, '*', 6, 6, '*', '+', 2000, '*']

def postfix_eval_expr(expr4):
    #expr4 = [3, 300, '*', 6, 6, '*', '+', 2000, '*']
    operand_stack = []
    for element in expr4:
        if element != '*' and element != '+':
            operand_stack.append(element)
        else:
            if element == '*':
                new = operand_stack.pop() * operand_stack.pop()
                operand_stack.append(new)
            if element == '+':
                new = operand_stack.pop() + operand_stack.pop()
                operand_stack.append(new)
    return operand_stack[0]  #1,872,000


expr2 = infix('( ( H2O ) 300 ( AM4B ) 6 ) 2000')
expr3 = postfix(expr2)
expr4 = eval_str(expr3)
postfix_eval_expr(expr4)