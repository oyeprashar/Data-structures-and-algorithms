"""
DFS + backtrack the visited array
"""
from collections import defaultdict

class Graph:
	def __init__(self,V):
		self.V = V 
		self.adj = defaultdict(list)
	
	def addEdge(self,u,v,cost):
		self.adj[u].append((v,cost))
		self.adj[v].append((u,cost))
	
	def isPossible(self,currV,currCost,visited,k):
		
		
		visited[currV] = True
		if currCost >= k:
			return True

		for list1 in self.adj[currV]:
			nbr = list1[0]
			
			edgeCost = list1[1]
			
			if visited[nbr] == False:
			
				if self.isPossible(nbr,currCost+edgeCost,visited,k) == True:
					return True

		visited[currV] = False
		return False 
	
	def check(self,src,k):
		visited = [False] * self.V
		return self.isPossible(src,0,visited,k)

V = 9
g = Graph(V)

g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

src = 0
k = 62
if g.check(src, k):
	print("Yes")
else:
	print("No")

k = 60
if g.check(src, k):
	print("Yes")
else:
	print("No")