#!/usr/bin/python3
import random, sys
n = int(sys.argv[1])

print(n)
for n in range(1, n):
    print(n + 1, random.randint(1, n))
