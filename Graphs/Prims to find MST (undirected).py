"""
Prims algo
"""
from collections import defaultdict
INT_MAX = 3**38

class Graph:

	def __init__(self,V):
		self.V = V
		self.vertList = defaultdict(list)
	
	def addEdge(self,u,v,cost):
		self.vertList[u].append((v,cost))
		self.vertList[v].append((u,cost))

	def pickMinVertex(self,value,visited):

		selected = None
		minCost = 3**38

		for v in range(len(value)):
			if value[v] < minCost  and v not in visited:
				selected = v
				minCost = value[v]
		
		return selected

	def prims(self):

		value = [INT_MAX] * self.V 
		value[0] = 0 
		
		visited = set()

		for _ in range(self.V):

			currV = self.pickMinVertex(value,visited)
			visited.add(currV)

			for list1 in self.vertList[currV]:

				nbr = list1[0]
				edgeCost = list1[1]

				if nbr not in visited:
					value[nbr] = min(value[nbr],edgeCost)
		
		return value,sum(value)
				
g = Graph(4)
g.addEdge(0,1,3)
g.addEdge(0,2,1)
g.addEdge(1,2,2)
g.addEdge(1,3,4)
g.addEdge(2,3,5)
print(g.prims())
				

			
