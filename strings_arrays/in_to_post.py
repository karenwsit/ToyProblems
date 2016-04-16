"""
Transform infix to postfix expression
"""
def in_to_post(exp):
    """
    >>> in_to_post("( A + B ) * ( C + D )")
    'A B + C D + *'
    >>> in_to_post("( A + B ) * C")
    'A B + C *'
    >>> in_to_post("A + B * C")
    'A B C * +'
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec[")"] = 10
    exp_list = exp.split()
    op_stack = []
    output_list = []
    for char in exp_list:
        if char not in prec:
            output_list.append(char)
        elif char == "(":
            op_stack.append(char)
        elif char == ")":
            top = op_stack.pop(-1)
            while top != "(":
                output_list.append(top)
                top = op_stack.pop(-1)
        else:
            while len(op_stack) != 0 and prec[op_stack[-1]] >= prec[char]:
                output_list.append(op_stack.pop(-1))
            op_stack.append(char)
        
    while len(op_stack) != 0:
        output_list.append(op_stack.pop(-1))
    
    return " ".join(output_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
