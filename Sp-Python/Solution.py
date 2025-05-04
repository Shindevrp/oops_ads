import math

def detect_arbitrage():
    N, M = map(int, input().split())

    graph = []
    for _ in range(M):
        u, v, r = input().split()
        u, v = int(u), int(v)
        r = float(r)
        weight = -math.log(r)
        graph.append((u - 1, v - 1, weight))  

    distance = [float('inf')] * N
    distance[0] = 0  

    for _ in range(N - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            print("Arbitrage Opportunity Detected")
            return

    print("No Arbitrage Opportunity")

detect_arbitrage()