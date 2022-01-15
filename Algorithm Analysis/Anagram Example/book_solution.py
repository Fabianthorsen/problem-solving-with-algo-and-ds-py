# Checking off
# This solution has O(n^2) time complexity
def anagram_solution1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1
    return still_ok


print("\nChecking off: ")
print(anagram_solution1("abcd", "dcba"))

# Sort and compare
# This solution has the same complexity as the sortings done
def anagram_solution2(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()  # These two determine the complexity, since they
    a_list2.sort()  # are either O(n log n) or O(n^2)

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


print("\nSort and compare: ")
print(anagram_solution2("abcd", "dcba"))

# Brute force
# Exhausts all possibilities. For this case, it would mean a compelxity of n!
# Exponential time complexity, very bad.

# Count and compare
# This has O(n) time complexity
# Althought this has a good time complexity, this sacrificed space to do so.
def anagram_solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok


print("\nCount and compare: ")
print(anagram_solution2("abcd", "dcba"))
