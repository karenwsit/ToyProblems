"""
Evaluate prefix mathematical expression and return value.

Implement a function 'int eval(String expr)' that evaluates expressions matching this syntax:
expr ::= int | '(' op expr+ ')'
op ::= '+' | '*'
So for example, these are syntactically-valid expressions:

"( + 1 2 )"
Output: '3'

"( + 3 4 5 )"
Output: '12'

"( + 7 ( * 8 12 ) ( * 2 ( + 9 4 ) 7 ) 3 )"
7 + (8 * 12)+(2* (9+4)*7*3)

The semantics are what you'd expect: ( * a b c ... ) evaluates to a * b * c * ..., and ( + a b c ... ) evaluates to a + b + c + ..., with integers evaluating to their own value. 
Tokens are all space-separated.

Sample Translation
"( + 3 4 ( * 7 12 ) 8 )" ----> "( 3 + 4 + ( 7 * 12 ) + 8 )"
"""

def eval(expr):
    list_expr = expr.split()
    op_stack = []
    int_stack = []

    i = 0
    while i < len(list_expr):
        if list_expr[i] == '(':
            i += 1
            op_stack.append(list_expr[i])
            i += 1
            int_stack.append(int(list_expr[i]))
        elif list_expr[i] == ')':
            op_stack.pop(-1)
            if len(op_stack) == 0:
                return int_stack[0]
            if op_stack[-1] == '+':
                int_stack[-2] = int(int_stack[-2]) + int(int_stack[-1])
            elif op_stack[-1] == '*':
                int_stack[-2] = int(int_stack[-2]) * int(int_stack[-1])
            int_stack.pop()
        else:
            if op_stack[-1] == '+':
                int_stack[-1] = int(int_stack[-1]) + int(list_expr[i])
            elif op_stack[-1] == '*':
                int_stack[-1] = int(int_stack[-1]) * int(list_expr[i])
        i += 1

print eval('( + 7 ( * 8 12 ) ( * 2 ( + 9 4 ) 7 ) 3 )')
