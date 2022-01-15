# Consider following expression:
# (A + B) * C - (D - E) * (F + G)
# Adding parenthesis to emphasis what goes when:
# (((A + B) * C) - ((D - E) * (F + G)))
# To Prefix:
# -*+ ABC *- DE + FG
# To Postfix:
# AB + C * DE - FG +*-

# The algorithm works as following:
# 1. Create a stack called op_stack to keep operators. Empty list for output
# 2. Convert input infix string to a list by using .split()
# 3. Scan token list from left -> right:
#   - If token is operand, append it to end of output list
#   - If token is left parens, push onto op_stack
#   - If token if right parens, pop op_stack untill left parens is removed
#   Append each operator to the end of output list
#   - If token is "*,/,+,-" push to op_stack. But first remove
#   any operators already on top of op_stack that have higher or equal
#   precedence and append them to output list.
# 4. When input has been scanned, check op_stack. If any ops left,
# append to the end of output list.

# For A*B+C*D - (A*B)+(C*D) it would become
# Input: A * B +   C *  D
# Stack: _ * * * + + *+ *+ *+ +
# Outpt: A   B   * C    D     * +
# Returns: AB*CD*+

from stack import Stack
from string import ascii_uppercase

# TODO: Add ability to use ** as token
def infix_to_postfix(expr: str) -> str:
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()
    postfix_list = []
    token_list = expr.split()

    # Iterate through all tokens in expression
    for token in token_list:

        # 1. If token is operand, append it to end of output list
        if token in ascii_uppercase or token in "0123456789":
            postfix_list.append(token)
        # 2. If token is left parens, push onto op_stack
        elif token == "(":
            op_stack.push(token)
        # If token if right parens, pop op_stack untill left parens is removed
        # Append each operator to the end of output list
        elif token == ")":
            top_token = op_stack.pop()

            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()

        # If token is "*,/,+,-" push to op_stack. But first remove
        # any operators already on top of op_stack that have higher or equal
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    # If any ops left, append to the postfix_list for output
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    # Return postfix expression
    return "".join(postfix_list)


print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
