from random import randrange
import math
print(sum([0 if math.sqrt((randrange(0, 100000) / 100000) ** 2 + (randrange(0, 100000) / 100000) ** 2) < 1 else 1 for _ in range(10000000)]) / 1000000 + 1)
