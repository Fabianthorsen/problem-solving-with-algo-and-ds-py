from stack import Stack


def divide_by_base(decimal: int, base: int) -> str:
    # Object with all possible digits to be used
    digits = "0123456789ABCDEF"

    #  Stack containing remainder
    rem_stack = Stack()

    #  While the decimal number is still not 0
    while decimal > 0:
        # Get the remainder
        rem = decimal % base
        # Add remainder to stack
        rem_stack.push(rem)
        # Decrement the decimal
        decimal = decimal // base

    # initialize the number string
    number_str = ""

    while not rem_stack.is_empty():
        # Pop to string untill stack is empty
        number_str += str(digits[rem_stack.pop()])

    return number_str


print(divide_by_base(25, 2))
print(divide_by_base(25, 8))
print(divide_by_base(25, 16))
