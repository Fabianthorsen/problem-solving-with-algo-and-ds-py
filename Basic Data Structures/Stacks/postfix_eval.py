# Funciton to evaluate postfix expressions
# Evaluation of postfix, left -> right:
# As example, if expression is 456*+, evaluating:
# Expr:  4 5 6  *  +
#        . . .  .  .
#        . . 6  .  .
#        . 5 5 30  .
# Stack: 4 4 4  4 34
#
# (push 4), (push 5), (push 6), (pop twice and do math), (pop twice and do math)
#
# With a more complex expression:
# Expr:  7 8  +  3  2  + /
#        . .  .  .  .  . .
#        . .  .  .  2  . .
#        . 8  .  3  3  5 .
# Stack: 7 7 15 15 15 15 3
#
# Algorithm works as follows:
# 1. Create empty stack called operand_stack
# 2. Convert string to a list, .split()
# 3. Scan left -> right
#   - If token is op, convert from string to int and push to operand_stack
#   - If token is an op, "*, /, +, -" it will need to operands. Pop operand_stack twice.
#       - First pop is second operand and second pop is first operand. Perform arithmetic op.
#   - Push the result back to operand_stack
# 4. When input has been scanned, result is on stack. Pop operand_stack and return.

from stack import Stack


def postfix_eval(expr: str) -> int:
    # Create empty stack called operand_stack, split expression
    operand_stack = Stack()
    token_list = expr.split()

    # Scan left -> right
    for token in token_list:

        # If token is op, convert from string to int and push to operand_stack
        if token in "0123456789":
            operand_stack.push(int(token))
        # If token is an op, "*, /, +, -" it will need to operands. Pop operand_stack twice.
        else:
            # First pop is second operand and second pop is first operand. Perform arithmetic op.
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            res = do_math(token, operand1, operand2)
            # Push the result back to operand_stack
            operand_stack.push(res)

    # Pop operand_stack and return.
    return operand_stack.pop()


# Helper function to evaluate expression
def do_math(op, op1, op2):
    if op == "*":
        return op1 + op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))
print(postfix_eval("4 5 6 * +"))
