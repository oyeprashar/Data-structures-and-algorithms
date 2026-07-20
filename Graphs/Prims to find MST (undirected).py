"""
**** Implement prims ****

Algo
	1. use a min heap (vertex, cost)
	2. While we have not selected all the vertices
		i. pop the top of min heap
	   ii. if not in visited, add to visited, add the cost
	  iii. Loop over the nbrs, and add them to heap if they are not visited


"""

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

        print("adj :",adj)

        minHeap = []
        heapq.heappush(minHeap, Item(0, 0))
        totalCost = 0
        visited = set()

        while len(minHeap) > 0 and V != 0:

            top = heapq.heappop(minHeap)

            totalCost += top.cost
            visited.add(top.vertex)
            V -= 1

            if V == 0:
                return totalCost

            for nbr in adj[top.vertex]:

                if nbr[0] not in visited:
                    heapq.heappush(minHeap, Item(nbr[0], nbr[1]))

        return totalCost

s = Solution()
print(s.spanningTree(V = 3, edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))