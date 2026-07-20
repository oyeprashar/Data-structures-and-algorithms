import heapq
from collections import defaultdict

class Item:

    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

    def __lt__(self, other):
        return self.cost <= other.cost


class Solution:
    def spanningTree(self, V, edges):

        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            edgeCost = edge[2]
            adj[u].append([v, edgeCost])
            adj[v].append([u, edgeCost])

        minHeap = []
        heapq.heappush(minHeap, Item(0, 0))
        totalCost = 0
        visited = set()

        # TC : O(eloge) because we are processes the edges in the heap
        #      len(visited) < V also depends on these edges
        while len(minHeap) > 0 and len(visited) < V:

            top = heapq.heappop(minHeap)
            
            if top.vertex in visited:
                continue

            totalCost += top.cost
            visited.add(top.vertex)

            for nbr in adj[top.vertex]:

                if nbr[0] not in visited:
                    heapq.heappush(minHeap, Item(nbr[0], nbr[1]))

        return totalCost
