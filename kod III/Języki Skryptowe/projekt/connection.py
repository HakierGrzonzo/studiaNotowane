import math

class Connection:
    def __init__(self, city1, city2) -> None:
        self.cities = (city1, city2)
        for city in self.cities:
            city.connections.append(self)

    def __repr__(self) -> str:
        return "{} <-> {}".format(
                self.cities[0].id + 1,
                self.cities[1].id + 1)
    def get_cities_with_distance(self, touched = None) -> dict:
        if touched is None:
            touched = list()
        res = {}
        new_touched = touched.copy()
        for city in self.cities:
            if city in touched:
                continue
            else:
                new_touched.append(city)
                res[city] = 1
                for connection in city.connections:
                    if connection is self:
                        continue
                    else:
                        tmp = connection.get_cities_with_distance(
                            new_touched
                        )
                        for dest, distance in tmp.items():
                            # TODO(add closest destinations)
                            distance += 1
                            res[dest] = min(distance, res.get(dest, math.inf))
        return res

    def get_other(self, city):
        if not city in self.cities:
            raise Exception("City not in connection!")
        if city is self.cities[0]:
            return self.cities[1]
        else:
            return self.cities[0]

    def get_dot_string(self) -> str:
        return f"{self.cities[0].id + 1} -- {self.cities[1].id + 1};"
