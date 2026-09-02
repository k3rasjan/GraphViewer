class Node:
    __count: int = 0

    def __init__(self, name: str | None = None) -> None:
        Node.__count += 1

        print("New Node object created!")

        self.id: int = Node.__count
        if name is None:
            self.name: str = f"Node{self.id}"
        else:
            self.name = name


class Graph:
    def __init__(self) -> None:
        self.nodes: list[Node] = []
        self.adjacencies: dict[Node, list[Node]] = {}

    def has_node(self, node: Node) -> bool:

        return node in self.nodes

    def add_node(self, node: Node) -> bool:
        if self.has_node(node):
            return False
        self.nodes.append(node)
        return True

    def add_adjacency(self, node1: Node, node2: Node) -> bool:
        if not self.has_node(node1) or not self.has_node(node2):
            return False

        if node1 not in self.adjacencies.keys():
            self.adjacencies[node1] = []

        if node2 in self.adjacencies[node1]:
            return False

        self.adjacencies[node1].append(node2)
        return True

    def remove_node(self, node: Node) -> bool:
        if self.has_node(node):
            self.nodes.remove(node)
            if node in self.adjacencies.keys():
                _ = self.adjacencies.pop(node)
            for adjacency in self.adjacencies.keys():
                edges = self.adjacencies.get(adjacency)
                if edges and node in edges:
                    edges.remove(node)
            return True
        return False

    def has_adjacency(self, node1: Node, node2: Node) -> bool:
        if not self.has_node(node1) or not self.has_node(node2):
            return False

        if node1 not in self.adjacencies.keys():
            return False

        edges = self.adjacencies.get(node1)

        if not edges:
            return False

        if node2 not in edges:
            return False

        return True

    def remove_adjacency(self, node1: Node, node2: Node) -> bool:
        if self.has_adjacency(node1, node2):
            edges = self.adjacencies.get(node1)
            if not edges:
                return False

            edges.remove(node2)
            return True
        return False

    def get_neighbours(self, node: Node) -> list[Node]:

        return self.adjacencies.get(node) or []


# node1 = Node()
# node2 = Node()
# graph = Graph()
#
# print(graph.add_node(node1))
# print(graph.add_node(node2))
# print(graph.add_adjacency(node1, node2))
# print(graph.has_node(node1))
# print(graph.has_adjacency(node1, node2))
# print(graph.get_neighbours(node1)[0])
# print(graph.get_neighbours(node2))
# print(graph.remove_node(node2))
# print(graph.has_node(node2))
