import sys
from datetime import datetime
from miasto import Miasto
from connection import Connection

num_of_cities = input()
cities = list([Miasto(x) for x in range(int(num_of_cities))])
connections = list()
for line in sys.stdin:
    first, second = [int(x) for x in line.split(" ")]
    connection = Connection(cities[first - 1], cities[second - 1])
    connections.append(connection)


def helper(city):
    return city.get_hotels()

#print(list([city.connections for city in cities]))
begin_time = datetime.now()
black_list = list()
res = 0
for city in cities:
    if city not in black_list:
        num, visited = city.get_hotels()
        res += num
        black_list += visited
print("Zajeło:", (datetime.now() - begin_time).total_seconds(), "s")
print(res)

with open("graph.dot", "w+") as f:
    f.write("graph {overlap=false;\n")
    f.write("\n\t".join([connection.get_dot_string() for connection in connections]))
    f.write("}")

