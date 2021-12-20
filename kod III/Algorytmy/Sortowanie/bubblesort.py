from typing import List 
def bubbleSort(A: List):
    n = len(A)
    while True:
        swapped = False
        for i in range(1, n):
            if A[i-1] > A[i]: 
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
        if not swapped: 
            return A
