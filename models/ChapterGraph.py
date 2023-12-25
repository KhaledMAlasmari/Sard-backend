class Graph:
    def __init__(self, id: int):
        self.id = id
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []

        # Store a tuple (node, weight) for the directed edge
        self.graph[u].append((v, weight))

    def remove_edge(self, u, v):
        """ Remove the edge from node u to node v. """
        if u in self.graph:
            self.graph[u] = [edge for edge in self.graph[u] if edge[0] != v]

    def get_adjacent_nodes(self, u):
        """ Return a list of nodes that u points to, along with their respective weights. """
        return self.graph.get(u, [])

    def __str__(self):
        return f"Graph {self.id}: {str(self.graph)}"

