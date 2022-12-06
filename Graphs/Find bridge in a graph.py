"""
Finding bridges in a graph

>> Method1
One by one remove each edge and see if it increases the components of the graph | Time complexity = O(E*(V+E))
(COMMENTED CODE)

>> Method2
Finding out if a node can be visited from some other path if it cannot than there is a bridge 
(CODE WITH BETTER IN FUNCTION NAME)

""" 
from collections import defaultdict 

class Graph:
	
	def __init__(self,V):
		self.V = V
		self.vertList = defaultdict(list)
	
	def addEdge(self,u,v):
		self.vertList[u].append(v)
		self.vertList[v].append(u)

	
	
	# def DFS(self,currV,exNode1,exNode2,visited):

	# 	visited.add(currV)
	
	# 	for nbr in self.vertList[currV]:
			
	# 		if nbr not in visited:
	# 			if (currV == exNode1 and nbr == exNode2) or (currV == exNode2 and nbr == exNode1):
	# 				continue 
	# 			else:
	# 				self.DFS(nbr,exNode1,exNode2,visited)

			
	# def countComponents(self,exNode1,exNode2):

	# 	count = 0
	# 	visited = set()

	# 	for currV in range(self.V):
	# 		if currV not in visited:
	# 			count += 1
	# 			self.DFS(currV,exNode1,exNode2,visited)


	# 	return count

	# def countBridges(self):
	# 	ans = []

	# 	for node1 in self.vertList:
	# 		for node2 in self.vertList[node1]:
	# 			currCount = self.countComponents(node1,node2)
	# 			if currCount > 1:
	# 				ans.append([node1,node2])
			
	# 	return sorted(ans)

	def findBridgesHelper(self,currV,currTime,initialTime,shortestTime,parent,visited):

		visited.add(currV)
		initialTime[currV] = currTime[0]
		shortestTime[currV] = currTime[0]

		currTime[0] += 1


		for nbr in self.vertList[currV]:
			if nbr not in visited:
				parent[nbr] = currV
				self.findBridgesHelper(nbr,currTime,initialTime,shortestTime,parent,visited)

		for nbr in self.vertList[currV]:
			if parent[currV] != nbr:
				shortestTime[currV] = min(shortestTime[currV],shortestTime[nbr])
				if shortestTime[nbr] > initialTime[currV]:
					# there is no another path and there is a single
					# edge here!!!

					print("Bridge found between",currV,"and",nbr)

	def findBridgesBetter(self):
		currTime = [1]
		initialTime = [3**38] * self.V
		shortestTime = [3**38] * self.V 
		visited = set()
		parent = [None] * self.V 
		self.findBridgesHelper(0,currTime,initialTime,shortestTime,parent,visited)
		# print(initialTime)
		# print(shortestTime)

	
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
 
  
print("Bridges in first graph ")
g1.findBridgesBetter()
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nBridges in second graph ")
g2.findBridgesBetter()
 
  
g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nBridges in third graph ")
g3.findBridgesBetter()



