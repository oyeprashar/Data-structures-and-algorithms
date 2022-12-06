"""
Input: digraph[V][V] = { {0, 0, 1, 0},
                        {1, 0, 0, 1},
                        {0, 1, 0, 0},
                        {0, 0, 1, 0}
                      };
Output: 2
Give adjacency matrix represents following 
directed graph.
"""
def findTriangles(adj,V,directed):

	count = 0

	for i in range(V):
		for j in range(V):

			for k in range(V):

				if adj[i][j] == 1 and adj[j][k] == 1 and adj[k][i] == 1:
					count += 1 
	
	if directed == True:
		return count // 3 
	
	else:
		return count // 6

adj =  [[0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0]]
		
print(findTriangles(adj,4,directed=True))