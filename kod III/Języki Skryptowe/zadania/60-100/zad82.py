from statistics import median, mean
from sys import argv
print(*[f([int(x) for x in open(argv[1]).readlines()]) for f in [sum, mean, median]], sep="\n")
