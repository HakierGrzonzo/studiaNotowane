import math
class Miasto:
    def __init__(self, id) -> None:
        self.id = id
        self.connections = []

    def __repr__(self) -> str:
        return f"Miasto {self.id + 1}"

    def get_connections(self) -> dict:
        initial_touched = [self]
        res = {}
        for connection in self.connections:
            for dest, distance in connection.get_cities_with_distance(
                    initial_touched
                ).items():
                res[dest] = min(distance, res.get(dest, math.inf))
        return res

    def get_hotels(self):
        black_list = list()
        dist_to_cities = {}
        for dest, dist in self.get_connections().items():
            array = dist_to_cities.get(dist, list())
            array.append(dest)
            dist_to_cities[dist] = array
        res = 0
        for _, array in dist_to_cities.items():
            if len(array) == 2:
                black_list += array
                res += 1
            elif (n := len(array)) > 2:
                black_list += array
                res += math.comb(n, 2)
        return res, black_list

