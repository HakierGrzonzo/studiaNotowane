class Node:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    @property
    def weight(self):
        return self.left.weight + self.right.weight

    def __repr__(self) -> str:
        return f"<({self.left} | {self.right})>"

    def getCode(self):
        res = dict()
        if isinstance(self.right, Node):
            for k, v in self.right.getCode().items():
                res["1" + k] = v
        else:
            res["1"] = self.right.symbol
        if isinstance(self.left, Node):
            for k, v in self.left.getCode().items():
                res["0" + k] = v
        else:
            res["0"] = self.left.symbol
        return res


class SymbolNode:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
    def __repr__(self) -> str:
        return f"<{self.symbol}: {self.weight}>"

def huffman(string: str):
    nodes = list([SymbolNode(x, string.count(x)) for x in set(string)])
    while len(nodes) > 1:
        newNodes = []
        sorted_node = sorted(nodes, key = lambda item: -item.weight)
        n1, n2 = sorted_node[-2:]
        others = sorted_node[:-2]
        nodes = others + [Node(n1, n2)]
    return nodes[0].getCode()

if __name__ == "__main__":
    print(huffman("hewwo"))
    print(huffman("to be or not to be"))
