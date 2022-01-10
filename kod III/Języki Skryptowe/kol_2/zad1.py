
class Macierz:
    def __init__(self, data) -> None:
        self.data = data

    def __add__(self, other):
        if self.getSize() != other.getSize():
            raise Exception("Not implemented")
        return Macierz(list([list([a + b for a, b in zip(rowA, rowB)]) for rowA, rowB in zip(self.data, other.data)]))

    def __sub__(self, other):
        if self.getSize() != other.getSize():
            raise Exception("Not implemented")
        return Macierz(list([list([a - b for a, b in zip(rowA, rowB)]) for rowA, rowB in zip(self.data, other.data)]))

    def invert(self):
        det = self.det()
        if det == 0:
            raise FloatingPointError
        else:
            det = 1 / det
            return Macierz(list([list([a * det for a in row]) for row in self.data]))

    def __repr__(self) -> str:
        return "Macierz:\n"+"\n".join(["\t".join([str(x) for x in row]) for row in self.data]) + "\n"

    def getSize(self):
        return [len(self.data), min([len(x) for x in self.data])]

    def det(self):
        if (size := self.getSize()) == [2, 2]:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        elif size == [3, 3]:
            return self.data[0][2] * self.data[1][1] * self.data[2][0] + \
                    self.data[1][2] * self.data[2][1] * self.data[0][0] + \
                    self.data[2][2] * self.data[0][1] * self.data[1][0]
        else:
            raise Exception("Not implemented")

if __name__ == "__main__":
    mats = [Macierz([[1, 3], [1, 2]]),
            Macierz([[1, 2, 3], [4, 5, 6], [0, 1, 1]]),
            Macierz([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            ]
    for a in mats:
        print(a)
        print("a + a", a + a)
        print("a - a", a - a)
        print("a + a - a", a + a - a)
        print("Odwrotność:", a.invert())
