import heapq

class DirectedConnection:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

    def from_node(self):
        return self.src

    def to_node(self):
        return self.dest

    def __str__(self):
        return f"{self.src}->{self.dest}  {self.cost:.2f}"

class WeightedDiGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency = [[] for _ in range(num_vertices)]

    def insert_edge(self, connection):
        self.adjacency[connection.from_node()].append(connection)

class DijkstraShortestPath:
    def __init__(self, graph, start):
        self.min_distance = [float('inf')] * graph.num_vertices
        self.path_trace = [None] * graph.num_vertices
        self.priority_queue = []
        self.min_distance[start] = 0.0
        heapq.heappush(self.priority_queue, (0.0, start))

        while self.priority_queue:
            _, current = heapq.heappop(self.priority_queue)
            for edge in graph.adjacency[current]:
                self._update_path(edge)

    def _update_path(self, edge):
        u, v = edge.from_node(), edge.to_node()
        if self.min_distance[v] > self.min_distance[u] + edge.cost:
            self.min_distance[v] = self.min_distance[u] + edge.cost
            self.path_trace[v] = edge
            heapq.heappush(self.priority_queue, (self.min_distance[v], v))

    def is_reachable(self, vertex):
        return self.min_distance[vertex] < float('inf')

    def retrieve_path(self, vertex):
        if not self.is_reachable(vertex):
            return None
        path = []
        edge = self.path_trace[vertex]
        while edge is not None:
            path.append(edge)
            edge = self.path_trace[edge.from_node()]
        return list(reversed(path))

def load_graph_input():
    lines = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    vertices = int(lines[0])
    graph = WeightedDiGraph(vertices)
    for line in lines[2:]:
        u, v, wt = line.split()
        graph.insert_edge(DirectedConnection(int(u), int(v), float(wt)))
    return graph, 0

if __name__ == "__main__":
    graph, start_node = load_graph_input()
    shortest_path_solver = DijkstraShortestPath(graph, start_node)

    for vertex in range(graph.num_vertices):
        if shortest_path_solver.is_reachable(vertex):
            path = shortest_path_solver.retrieve_path(vertex)
            distance = shortest_path_solver.min_distance[vertex]
            print(f"{start_node} to {vertex} ({distance:.2f}) ", end=' ')
            if path:
                for edge in path:
                    print(f"{edge}", end='   ')
            print()
        else:
            print(f"{start_node} to {vertex}: no path")