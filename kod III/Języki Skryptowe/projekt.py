import sys
from miasto import Miasto
from connection import Connection

num_of_cities = input()
cities = list([Miasto(x) for x in range(int(num_of_cities))])
for line in sys.stdin:
    first, second = [int(x) for x in line.split(" ")]
    connection = Connection(cities[first], cities[second])

print(cities[0].connections)
