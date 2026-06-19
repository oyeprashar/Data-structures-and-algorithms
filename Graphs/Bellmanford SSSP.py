"""
Bellman Ford (handles -ve edges)

Unlike Dijkstra, we DONT keep visited  and relax all the edges for V times
"""

INT_MAX = 3**38

def bellman_ford(edges, number_of_nodes, src):

    distance = [INT_MAX] * number_of_nodes
    distance[src] = 0


    for _ in range(number_of_nodes):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            cost = edge[2]

            if distance[u] != INT_MAX:
                distance[v] = min( distance[v], distance[u] + cost)


    # another loop to detect negative cycle
    for edge in edges:
        u = edge[0]
        v = edge[1]
        cost = edge[2]

        if distance[u] + cost < distance[v]:
            return "negative cycle found"


    return distance


