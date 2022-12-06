from collections import defaultdict
INT_MAX = 3**38

class Graph:
	def __init__(self,V):
		self.V = V 
		self.adj = defaultdict(list)

	def addEdge(self,u,v):
		self.adj[u].append((v,0))
		self.adj[v].append((u,1))
		
	def pickMinV(self,visited,cost):

		minCost = 3**38
		selected = None

		for i in range(len(cost)):
			if cost[i] < minCost and i not in visited:
				minCost = cost[i]
				selected = i 
		
		return selected

	
	def dijsktra(self,src,dst):

		cost = [INT_MAX] * self.V
		cost[src] = 0
		visited = set()

		for _ in range(self.V):

			currV = self.pickMinV(visited,cost)
			visited.add(currV)
			
			for nbr,edgeCost in self.adj[currV]:
				
				if nbr not in visited:
					if cost[currV] + edgeCost < cost[nbr]:
						cost[nbr] = cost[currV] + edgeCost
		
		return cost[dst]


	def minEdges(self,src,dst):
		return self.dijsktra(src,dst)
		
				
	
g = Graph(7)
g.addEdge(0,1)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(6,3)
g.addEdge(6,4)
g.addEdge(4,5)
g.addEdge(5,1)

print(g.minEdges(0,6))


	
