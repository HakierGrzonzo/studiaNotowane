from typing import List
from sys import stdin

def bubbleSort(A: List):
    # do sortowanie trzech elementów
    n = len(A)
    while True:
        swapped = False
        for i in range(1, n):
            if A[i-1] > A[i]: 
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
        if not swapped: 
            return A

def quicksort(arr: List, sort_func) -> List:
    if len(arr) > 1:
        if len(arr) >= 3:
            p = sort_func(bubbleSort(arr[:3])[1])
        else:
            p = sort_func(arr[-1])
        return quicksort([x for x in arr if sort_func(x) < p], sort_func) + \
                list([x for x in arr if sort_func(x) == p]) + \
                quicksort([x for x in arr if sort_func(x) > p], sort_func)
    else:
        return list(arr)

def sort_func_generator(main_index):
    def sort_func(tasks):
        return tasks[main_index]
    return sort_func

if __name__ == "__main__":
    print("Podaj główne kryterium")
    indexes = int(input())
    print("Podaj dane w formacie a, b\\n")
    data = []
    for line in stdin:
        in_data = list([int(x.strip()) for x in line.split(",")])
        data.append(in_data)
    sort_func = sort_func_generator(indexes - 1)
    res = quicksort(data, sort_func)
    for x in res:
        print(",\t".join([str(y) for y in x]))

