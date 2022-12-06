"""
Two Clique problem
mat = [[0, 1, 1, 0, 0],
      [1, 0, 1, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 0, 1, 0]]
Output : Yes
"""

from collections import defaultdict

def isBipartite(src,adj,colored):

	queue = [src]

	while len(queue) > 0:

		currV = queue.pop(0)

		available = [True,True]

		for nbr in adj[currV]:
			if colored[nbr] == -1:
				queue.append(nbr)

			else:
				available[colored[nbr]] = False

		selectedColor = None
		for i in range(len(available)):
			if available[i] == True:
				selectedColor = i 
				break 
		
		if selectedColor == None:
			return False 
		
		colored[currV] = selectedColor
	
	return True 

def isTwoClique(mat):

	V = len(mat)

	adj = defaultdict(list)

	for row in range(len(mat)):
		for col in range(len(mat)):

			if mat[row][col] == 0 and row != col:
				adj[row].append(col)
				adj[col].append(row)
	
	colored = [-1] * V

	for currV in range(V):
		if colored[currV] == -1:
			if isBipartite(currV,adj,colored) == False:
				return False 
			
	return True 

mat = [[0, 1, 1, 0, 0],
      [1, 0, 1, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 0, 1, 0]]

print(isTwoClique(mat))


