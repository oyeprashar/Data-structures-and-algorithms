"""
grid = [['S','.','.','#','.','.','.'],
	    ['.','#','.','.','.','#','.'],
	    ['.','#','.','.','.','.','.'],
	    ['.','.','#','#','.' ,'.', '.'],
	    ['#','.','#','E','.','#','.']]


"""

def shortestPath(sr,sc,grid):

	dr = [-1,+1,0,0]
	dc = [0,0,-1,+1]

	visited = []
	for x in range(len(grid)):
		list1 = []
		for y in range(len(grid[0])):
			list1.append(False)
		visited.append(list1)

	distance = []
	for x in range(len(grid)):
		list1 = []
		for y in range(len(grid[0])):
			list1.append(0)
		distance.append(list1)


	queue = []
	queue.append((sr,sc))
	visited[sr][sc] = True

	while len(queue) != 0:


		curr = queue.pop(0)
		currR = curr[0]
		currC = curr[1]
	

		for i in range(len(dr)):
			nbrR = currR + dr[i]
			nbrC = currC + dc[i]

			if nbrR >= 0 and nbrC >= 0 and nbrR < len(grid) and nbrC < len(grid[0]):
				
				if grid[nbrR][nbrC] != "#" and visited[nbrR][nbrC] != True:
					queue.append((nbrR,nbrC))
					distance[nbrR][nbrC]  = 1 + distance[currR][currC]
					visited[nbrR][nbrC] = True

					if grid[nbrR][nbrC] == "E":
						return distance[nbrR][nbrC]

	return -1

	

grid = [['S','.','.','#','.','.','.'],
	    ['.','#','.','.','.','#','.'],
	    ['.','#','.','.','.','.','.'],
	    ['.','.','#','#','.' ,'.', '.'],
	    ['#','.','#','E','.','#','.']]

# grid = [['S','.','.','.','.','.','.'],
# 	    ['.','.','.','.','.','.','.'],
# 	    ['.','.','.','.','.','.','.'],
# 	    ['.','.','.','.','.' ,'.', '.'],
# 	    ['.','.','.','E','.','.','.']]






print(shortestPath(0,0,grid))
