class Graph:
    """
    Graph using adjacency list representation.
    """

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a new vertex."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        """Add edge between v1 and v2."""
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def display(self):
        """Display adjacency list."""
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])
