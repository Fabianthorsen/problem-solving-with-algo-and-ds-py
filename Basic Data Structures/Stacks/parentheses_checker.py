from stack import Stack


def par_checker(symbol_string: str) -> bool:
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        # Set current char as symbol
        symbol = symbol_string[index]

        # If symbol is a left parenthesis, left square bracket or left bracket
        if symbol in "([{":
            # Push to stack
            s.push(symbol)
        else:

            # If not a left, stack is empty
            if s.is_empty():
                # The string isn't balanced
                balanced = False
            else:
                # If not empty then we pop one item from stack
                top = s.pop()

                # Check if the top of stack, matches the current: ( or [ or {
                if not matches(top, symbol):
                    # Un-balanced if no match
                    balanced = False

        # Increment index once, and re-run
        index += 1

    # After iteration, if balanced and stack is empty
    if balanced and s.is_empty():
        # The string is balanced
        return True
    else:
        # Else it is not balanced
        return False


def matches(open: str, close: str) -> bool:
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(par_checker("{{([][])}()}"))  # Balanced
print(par_checker("[{()]"))  # Un-balanced
