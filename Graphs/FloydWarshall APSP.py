"""
-> loop to select an intermediate node
    -> loop to select a source
        -> loop to select a destination
"""

INT_MAX = 3**38
def floydWarshall(adj):

	dist = []

	for i in range(len(adj)):
		list1 = []
		for j in range(len(adj)):
			list1.append(adj[i][j])
		dist.append(list1)

	for k in range(len(adj)):
		for i in range(len(adj)):
			for j in range(len(adj)):

				dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
			

	for x in range(len(adj)):
		if dist[x][x] < 0:
			return "NEGATIVE CYCLE FOUND!"
		
	
	return dist


adj =  [[0,5,INT_MAX,10],
		[INT_MAX,0,3,INT_MAX],
		[INT_MAX,INT_MAX,0,1],
		[INT_MAX,INT_MAX,INT_MAX,0]]
	
ans = floydWarshall(adj)

for row in ans:
	print(row)
