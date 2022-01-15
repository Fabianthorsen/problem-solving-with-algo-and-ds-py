from stack import Stack


def divide_by_two(decimal: int) -> str:
    #  Stack containing remainder
    rem_stack = Stack()

    #  While the decimal number is still not 0
    while decimal > 0:
        # Get the remainder
        rem = decimal % 2
        # Add remainder to stack
        rem_stack.push(rem)
        # Decrement the decimal
        decimal = decimal // 2

    # initialize the binary string
    bin_str = ""

    while not rem_stack.is_empty():
        # Pop to string untill stack is empty
        bin_str += str(rem_stack.pop())

    return bin_str


print(divide_by_two(123))
