from stack import Stack

# Write a function rev_string(string) that uses a stack
# to reverse a string


def rev_string(string: str) -> str:
    s = Stack()
    rev = []

    # Populate the stack
    for l in string:
        s.push(l)

    # Pop from s until it is empty
    while not s.is_empty():
        rev.append(s.pop())

    return "".join(rev)


print(rev_string("My String"))
