import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, vertex):
        return self.w if vertex == self.v else self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"{self.v}-{self.w} ({self.weight})"


class EdgeWeightedGraph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)

    def adjacent(self, v):
        return self.adj[v]


class LazyPrimMST:
    def __init__(self, graph):
        self.marked = [False] * graph.V
        self.mst = []
        self.pq = []
        self.total_weight = 0.0

        for v in range(graph.V):  
            if not self.marked[v]:
                self.prim(graph, v)

    def prim(self, graph, s):
        self.scan(graph, s)
        while self.pq:
            weight, edge = heapq.heappop(self.pq)
            v = edge.either()
            w = edge.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append(edge)
            self.total_weight += edge.weight
            if not self.marked[v]:
                self.scan(graph, v)
            if not self.marked[w]:
                self.scan(graph, w)

    def scan(self, graph, v):
        self.marked[v] = True
        for edge in graph.adjacent(v):
            if not self.marked[edge.other(v)]:
                heapq.heappush(self.pq, (edge.weight, edge))

    def edges(self):
        return self.mst

    def weight(self):
        return self.total_weight



def main():
    V = int(input())  
    E = int(input()) 

    graph = EdgeWeightedGraph(V)

    for _ in range(E):
        v, w, weight = input().split()
        graph.add_edge(Edge(int(v), int(w), float(weight)))

    mst = LazyPrimMST(graph)

    weight = mst.weight()
    if weight == int(weight):
        print(f"{weight:.1f}")
    else:
        print(f"{weight:.2f}")



if __name__ == "__main__":
    main()