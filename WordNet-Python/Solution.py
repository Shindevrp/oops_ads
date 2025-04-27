import sys
from collections import defaultdict, deque

class Digraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = defaultdict(list)

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.E += 1

    def adjacent(self, v):
        return self.adj[v]

    def reverse(self):
        reverse_graph = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                reverse_graph.add_edge(w, v)
        return reverse_graph

    def has_cycle(self):
        visited = [False] * self.V
        on_stack = [False] * self.V

        def dfs(v):
            visited[v] = True
            on_stack[v] = True
            for w in self.adjacent(v):
                if not visited[w]:
                    if dfs(w):
                        return True
                elif on_stack[w]:
                    return True
            on_stack[v] = False
            return False

        for v in range(self.V):
            if not visited[v]:
                if dfs(v):
                    return True
        return False

class SAP:
    def __init__(self, G):
        self.G = G

    def bfs(self, sources):
        dist = [-1] * self.G.V
        queue = deque()
        for s in sources:
            dist[s] = 0
            queue.append(s)

        while queue:
            v = queue.popleft()
            for w in self.G.adjacent(v):
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        return dist

    def _sap(self, v, w):
        if isinstance(v, int): v = [v]
        if isinstance(w, int): w = [w]

        dist_v = self.bfs(v)
        dist_w = self.bfs(w)

        min_dist = float('inf')
        ancestor = -1

        for i in range(self.G.V):
            if dist_v[i] != -1 and dist_w[i] != -1:
                total_dist = dist_v[i] + dist_w[i]
                if total_dist < min_dist:
                    min_dist = total_dist
                    ancestor = i

        return (min_dist if ancestor != -1 else -1, ancestor)

    def length(self, v, w):
        return self._sap(v, w)[0]

    def ancestor(self, v, w):
        return self._sap(v, w)[1]

class WordNet:
    def __init__(self, synsets_file, hypernyms_file):
        if not synsets_file or not hypernyms_file:
            raise ValueError("Input files cannot be null")

        self.id_to_synset = {}
        self.noun_to_ids = defaultdict(set)

        with open(synsets_file) as f:
            for line in f:
                parts = line.strip().split(',')
                synset_id = int(parts[0])
                nouns = parts[1].split()
                self.id_to_synset[synset_id] = parts[1]
                for noun in nouns:
                    self.noun_to_ids[noun].add(synset_id)

        self.G = Digraph(len(self.id_to_synset))

        with open(hypernyms_file) as f:
            for line in f:
                parts = list(map(int, line.strip().split(',')))
                synset_id = parts[0]
                for hypernym_id in parts[1:]:
                    self.G.add_edge(synset_id, hypernym_id)

        if self.G.has_cycle():
            print("Cycle detected")
            sys.exit(0)

        roots = [v for v in range(self.G.V) if len(self.G.adjacent(v)) == 0]
        if len(roots) != 1:
            print("Multiple roots")
            sys.exit(0)

        self.sap_obj = SAP(self.G)

    def nouns(self):
        return self.noun_to_ids.keys()

    def is_noun(self, word):
        if word is None:
            raise ValueError("word is null")
        return word in self.noun_to_ids

    def distance(self, nounA, nounB):
        if not self.is_noun(nounA) or not self.is_noun(nounB):
            raise ValueError("Invalid noun")
        return self.sap_obj.length(self.noun_to_ids[nounA], self.noun_to_ids[nounB])

    def sap(self, nounA, nounB):
        if not self.is_noun(nounA) or not self.is_noun(nounB):
            raise ValueError("Invalid noun")
        ancestor_id = self.sap_obj.ancestor(self.noun_to_ids[nounA], self.noun_to_ids[nounB])
        return self.id_to_synset[ancestor_id] if ancestor_id != -1 else None

def main():
    synsets = input().strip()
    hypernyms = input().strip()
    command = input().strip()

    wn = WordNet(synsets, hypernyms)

    if command == "Graph":
        print(f"{wn.G.V} vertices, {wn.G.E} edges ")
        for v in range(wn.G.V):
            adj = wn.G.adjacent(v)
            if adj:
                print(f"{v}: {' '.join(map(str, sorted(adj, reverse=True)))} ")
            else:
                print(f"{v}: ")
        print()
    elif command == "Queries":
        try:
            while True:
                line = input().strip()
                if not line:
                    break
                nounA, nounB = line.split()
                try:
                    dist = wn.distance(nounA, nounB)
                    ancestor = wn.sap(nounA, nounB)
                    print(f"distance = {dist}, ancestor = {ancestor}")
                except ValueError:
                    print("IllegalArgumentException")
        except EOFError:
            pass

if __name__ == "__main__":
    main()