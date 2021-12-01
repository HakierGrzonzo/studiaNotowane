from statistics import median, mean
from sys import stdin
l = list([int(x) for x in stdin])
print(*[f(l) for f in [sum, mean, median]], sep="\n")
