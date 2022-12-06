"""
Graph Colouring Problem
"""
from collections import defaultdict

class Graph:
	def __init__(self,V):
		self.V = V
		self.verList = defaultdict(list)
	
	def addEdge(self,u,v):
		self.verList[u].append(v)
		self.verList[v].append(u)
	
	def chromaticNumber(self):
		
		maxColor = 0
		colored = [-1] * (self.V + 1)
		queue = [0]
		visited = set()
		visited.add(0)

		while len(queue) > 0:

			print(queue)

			curr = queue.pop(0)
			availColors = [True] * (self.V + 1)

			# find out the avail colors
			for nbr in self.verList[curr]:
				if nbr not in visited:
					queue.append(nbr)
					visited.add(nbr)
				else:
					currColor = colored[nbr]
					availColors[currColor] = False 
			
			# find out the smallest color that we can pick
			selectedColor = None
			for i in range(len(availColors)):
				if availColors[i] == True:
					selectedColor = i 
					break 
			
			# update the maxColor 
			colored[curr] = selectedColor
			maxColor = max(maxColor,selectedColor)
		
		return maxColor + 1
	
g1 = Graph(4)
g1.addEdge(0,1)
g1.addEdge(1,3)
g1.addEdge(3,2)
g1.addEdge(2,0)
g1.addEdge(2,4)
g1.addEdge(4,1)
print(g1.chromaticNumber())
