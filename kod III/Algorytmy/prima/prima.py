class Connection:
    def __init__(self, node1, node2, cost):
        self.nodes = (node1, node2)
        self.cost = cost
        for node in self.nodes:
            node.connections.append(self)

    def get_other(self, first):
        if self.nodes[0] is first:
            return self.nodes[1]
        else:
            return self.nodes[0]
    
    def __repr__(self):
        return f"{self.nodes[0].id} <-{self.cost}-> {self.nodes[1].id}"

class Node:
    def __init__(self, id):
        self.id = id
        self.connections = []

    def __repr__(self):
        return f"Node: {self.id}"
  
def dijkstra(start: Node, nodes: list[Node]):
    pred = dict()
    k = dict()
    for node in nodes:
        pred[node] = None
        k[node] = float('inf')
    k[start] = 0
    while len(nodes) > 0:
        node = sorted(nodes, key=lambda item: k[item])[0]
        nodes.remove(node)
        for connection in node.connections:
            other_node = connection.get_other(node)
            if other_node in nodes:
                if k[other_node] > connection.cost + k[node]:
                    k[other_node] = connection.cost + k[node]
                    pred[other_node] = node
    return k


def prima(nodes: list[Node]):
    pred = dict()
    k = dict()
    for node in nodes:
        pred[node] = None
        k[node] = float('inf')
    # wierzchołek startowy
    node = nodes[0]
    k[node] = 0
    while len(nodes) > 0:
        node = sorted(nodes, key=lambda item: k[item])[0]
        nodes.remove(node)
        for connection in node.connections:
            other_node = connection.get_other(node)
            if other_node in nodes:
                if k[other_node] > connection.cost:
                    k[other_node] = connection.cost
                    pred[other_node] = node
    res = []
    for node in pred.keys():
        if pred[node] is not None:
            res.append(Connection(node, pred[node], k[node]))
    return res

def main():
    # krawędzie w formie:
    # skąd dokąd kost
    raw_graf = """
1 2 3
1 4 3
1 5 5
2 3 5
2 4 1
3 4 2
5 4 1
    """
    nodes = list([Node(i) for i in range(1, 6)])
    connections = list()
    for line in raw_graf.strip().splitlines():
        node1, node2, cost = line.split(" ")
        connections.append(Connection(
            nodes[int(node1) - 1],
            nodes[int(node2) - 1], int(cost)))
    print(connections)
    print(prima(nodes.copy()))
    print(dijkstra(nodes[0] ,nodes.copy()))



if __name__ == "__main__":
    main()

