from typing import List, Optional
from bigO import BigO

# Write a funciton that takes O(n^2) to find minimum in a list
def list_min_quad(lst: List[int]) -> Optional[int]:
    min_val = None
    for i in lst:
        for j in lst:
            if min_val != None:
                if i < j and i < min_val:
                    min_val = i
                elif j < i and j < min_val:
                    min_val = j
            else:
                if i < j:
                    min_val = i
                else:
                    min_val = j
    return min_val


# Write a function that take O(n) to find minimum in a list
def list_min_lin(lst: List[int]) -> Optional[int]:
    min_val = None
    for i in lst:
        if min_val == None:
            min_val = i
        else:
            if i < min_val:
                min_val = i
    return min_val


print(list_min_quad([3, 5, 2, 3, 1, 6, -1, 5, -3]))
print(list_min_lin([3, 5, 2, 3, 1, 6, -1, 5, -3]))
