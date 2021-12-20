from bubblesort import bubbleSort
from insertsort import insertsort
from quicksort import quicksort

from random import randint
from typing import List
from datetime import datetime

def get_time_since(past: datetime):
    return (datetime.now() - past).total_seconds()

sorts = [quicksort, bubbleSort, insertsort]

def generate_list(size: int) -> List[int]:
    return list([randint(0, size * 2) for _ in range(size)])


def is_sorted(list: List):
    for a, b in zip(list, sorted(list)):
        if a != b:
            return False
    else:
        return True

small = generate_list(10)
medium = generate_list(1024)
large = generate_list(8192)
for sort in sorts:
    print("Testing", sort)
    for x in [small, medium, large]:
        tmp = x.copy()
        began_at = datetime.now()
        a = sort(tmp)
        time = get_time_since(began_at)
        print(len(x), "->", time, is_sorted(a))
