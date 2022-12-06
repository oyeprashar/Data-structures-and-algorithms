"""
Bellman-ford algo
"""
from collections import defaultdict 
INT_MAX = 3**38

class Graph:
	def __init__(self,V):
		self.V = V
		self.vertList = []
	
	def addEdge(self,u,v,cost):
		self.vertList.append((u,v,cost))
	
	def bellmanford(self):

		dist = [INT_MAX] * self.V 
		dist[0] = 0

		for _ in range(self.V):

			for list1 in self.vertList:
				u = list1[0]
				v = list1[1]
				cost = list1[2]

				if dist[u] + cost < dist[v]:
					dist[v] = dist[u] + cost 

		# checking for the negative cycles
		for list1 in self.vertList:
				u = list1[0]
				v = list1[1]
				cost = list1[2]

				if dist[u] + cost < dist[v]:
					return "NEGATIVE CYCLE FOUND"
						
		
				
		return dist 
	
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
print(g.bellmanford())

g1 = Graph(4)
g1.addEdge(0,1,1)
g1.addEdge(1,2,-1)
g1.addEdge(2,3,-1)
g1.addEdge(3,0,-1)
print(g1.bellmanford())