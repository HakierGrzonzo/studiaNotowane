from typing import List

def merge(a: List, b: List) -> List:
    index_a = 0
    index_b = 0
    res = []
    while index_a + 1 <= len(a) and index_b + 1 <= len(b):
        if a[index_a] <= b[index_b]:
            res.append(a[index_a])
            index_a += 1
        else:
            res.append(b[index_b])
            index_b += 1
    res += a[index_a:] + b[index_b:]
    return res


def mergesort(m : List) -> List:
    match len(m):
        case 1:
            return m
        case 2:
            return [min(m), max(m)]
        case _:
            divider = len(m) // 2 
            return merge(mergesort(m[divider:]), mergesort(m[:divider]))

if __name__ == "__main__":
    print(merge([1, 3, 10], [2, 11, 200]))
    print(mergesort([0, 13, -3, -2]))
