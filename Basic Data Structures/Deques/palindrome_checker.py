# A palindrome is a string that reads the same forwards and backwards
# - radar, toot, madam
# 1. Use deque to store chars of the string.
# 2. Process left -> right
#   - Remove and compare both rear and front
#       - Only continue if they match
# 3. At the end the deque will be either empty or 1
#   - If 1 the string was odd length, and is palindrome
#   - If empty string was even length, and is palindrome

from deque import Deque


def pal_checker(string: str) -> bool:
    char_deque = Deque[str]()

    # Populate the deque
    for char in string:
        char_deque.add_front(char)  # Add front since O(1) rather than O(n).

    still_equal = True

    # Process untill size is 1 or the ends doesn't match
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        # Not a palindrome if ends don't match
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("radar"))
print(pal_checker("fabian"))
