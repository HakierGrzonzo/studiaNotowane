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

    def get_other(self, city):
        if not city in self.cities:
            raise Exception("City not in connection!")
        if city is self.cities[0]:
            return self.cities[1]
        else:
            return self.cities[0]

    def get_dot_string(self) -> str:
        return f"{self.cities[0].id + 1} -- {self.cities[1].id + 1};"

