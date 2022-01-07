from typing import List

def heapify(l: List, size: int, index: int):
    largest = index
    left = 2 * index + 1
    right = left + 1
    if left < size and l[index] < l[left]:
        largest = left
    if right < size and l[largest] < l[right]:
        largest = right

    if largest != index:
        l[index], l[largest] = l[largest], l[index]
        heapify(l, size, largest)

def heapsort(l: List) -> List:
    size = len(l)
    for i in range(size // 2 - 1, -1, -1):
        heapify(l, size, i)
    for i in reversed(range(len(l))):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)
    return l

if __name__ == "__main__":
    print(heapsort([10, -2, 3, 99, -24]))



