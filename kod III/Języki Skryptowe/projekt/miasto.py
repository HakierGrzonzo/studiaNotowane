import math

class Miasto:
    def __init__(self, id) -> None:
        self.id = id
        self.connections = []
        self.city2distance = {}
        self.__quickmode = None
        self.locked = False

    def __repr__(self) -> str:
        return f"<Miasto {self.id + 1}>"

    def get_connections(self, force_slow = False):
        if self.__quickmode is not None and not force_slow:
            gateway, offset = self.__quickmode
            for city, distance in gateway.city2distance.items():
                if city not in self.city2distance.keys():
                    self.city2distance[city] = offset + distance
        elif len(self.city2distance.keys()) == 0:
            for connection in self.connections:
                self.city2distance[connection.get_other(self)] = 1
            if len(self.city2distance.keys()) == 1 and not self.locked:
                # encountered a node that connects us to everyone else
                self.__quickmode = list(self.city2distance.items())[0]
        else:
            max_distance = max(self.city2distance.values())
            tmp = {}
            for city, distance in self.city2distance.items():
                if distance == max_distance:
                    # only care about furthest cities
                    for candidate in city.get_surrounding_cities():
                        if candidate not in self.city2distance.keys():
                            tmp[candidate] = max_distance + 1
            if len(tmp.keys()) == 1 and not self.locked:
                # encountered a node that connects us to everyone else
                self.__quickmode = list(tmp.items())[0]
            for k, v in tmp.items():
                self.city2distance[k] = v

        return self.__quickmode is not None


    def get_surrounding_cities(self) -> list:
        res = list()
        for connection in self.connections:
            res.append(connection.get_other(self))
        return res

    def get_hotels(self):
        self.distance2city = {}
        res = []
        for city, distance in self.city2distance.items():
            if city.id > self.id:
                array = self.distance2city.get(distance, list())
                array.append(city)
                self.distance2city[distance] = array
        for distance, array in self.distance2city.items():
            if len(array) >= 2:
                for i, city in enumerate(array[:-1]):
                    if city is not self:
                        for another_city in array[i:]:
                            if (
                                    city.city2distance[another_city] == distance and 
                                    another_city is not self and
                                    city is not another_city):
                                hotel = [self.id, city.id, another_city.id]
                                hotel.sort()
                                hotel_str = ""
                                for x in hotel:
                                    hotel_str += "-" + str(x)
                                if not hotel_str in res:
                                    res.append(hotel_str)
        return res


