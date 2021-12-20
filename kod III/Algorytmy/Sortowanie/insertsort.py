from typing import List 
def insertsort(arr: List):
    res = []
    while len(arr) > 0:
        min = arr[0]
        index = 0
        for i, x in enumerate(arr):
            if x < min:
                min = x
                index = i
        del arr[index]
        res.append(min)
    return res

