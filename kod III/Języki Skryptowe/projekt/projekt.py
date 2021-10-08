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

begin_time = datetime.now()
done_cities = list()
iteration = 1
while len(done_cities) != len(cities):
    iteration += 1
    for city in cities:
        if city in done_cities:
            continue
        elif len(city.city2distance.keys()) == len(cities):
            done_cities.append(city)
        else:
            if city.get_connections():
                # city is in quick_mode
                done_cities.append(city)
    print(len(done_cities), iteration, file=sys.stderr, end="\r")

really_done_cities = list()
iteration = 0
print(file=sys.stderr)
while len(really_done_cities) < len(done_cities):
    did_modify_something = False
    for city in done_cities:
        print(len(really_done_cities), iteration, file=sys.stderr, end="\r")
        if city in really_done_cities:
            continue
        elif len(city.city2distance.keys()) == len(cities):
            really_done_cities.append(city)
            did_modify_something = True
        else:
            # finish cities in quick_mode
            city.get_connections()
    if not did_modify_something:
        for city in done_cities:
            if city in really_done_cities:
                continue
            city.get_connections(True)

print(file=sys.stderr)
hotels = []
for i, city in enumerate(really_done_cities):
    print(f"\33[2K{round(i / len(cities) * 100, 2)}%", len(hotels), file=sys.stderr, end="\r")
    new_hotels = city.get_hotels()
    for new_hotel in new_hotels:
        if new_hotel not in hotels:
            hotels.append(new_hotel)

print(file=sys.stderr)

print("Zajeło:", (datetime.now() - begin_time).total_seconds(), "s")
print(hotels)

"""
with open("graph.dot", "w+") as f:
    f.write("graph {overlap=false;\n")
    f.write("\n\t".join([connection.get_dot_string() for connection in connections]))
    f.write("}")
"""

