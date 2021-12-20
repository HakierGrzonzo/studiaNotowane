from typing import List, Iterable

def quicksort(arr: List) -> List:
    if len(arr) > 1:
        p = arr[-1]
        return quicksort([x for x in arr if x < p]) + \
                list([x for x in arr if x == p]) + \
                quicksort([x for x in arr if x > p])
    else:
        return list(arr)
