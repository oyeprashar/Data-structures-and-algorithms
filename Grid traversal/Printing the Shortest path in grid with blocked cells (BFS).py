def shortestPath(sr,sc,grid):

	dr = [-1,+1,0,0]
	dc = [0,0,-1,+1]

	visited = []
	for x in range(len(grid)):
		list1 = []
		for y in range(len(grid[0])):
			list1.append(False)
		visited.append(list1)

	queue = []
	queue.append((sr,sc))
	visited[sr][sc] = (0,0)

	found = False

	while len(queue) != 0:


		curr = queue.pop(0)
		currR = curr[0]
		currC = curr[1]



		if grid[currR][currC] == "E":
			found = True
			desti = currR
			destj = currC
			break


		for i in range(len(dr)):
			nbrR = currR + dr[i]
			nbrC = currC + dc[i]

			if nbrR >= 0 and nbrC >= 0 and nbrR < len(grid) and nbrC < len(grid[0]):
				
				if grid[nbrR][nbrC] != "#" and visited[nbrR][nbrC] == False:
					visited[nbrR][nbrC] = ((currR,currC))
					queue.append((nbrR,nbrC))

	if found == False:
		return -1
		
	path = []

	while desti != 0 or destj != 0:
		curr = visited[desti][destj]
		desti = curr[0]
		destj = curr[1]
		path.append((desti,destj))
		
	return path,len(path)

grid = [['S','.','.','#','.','.','.'],
	    ['.','#','.','.','.','#','.'],
	    ['.','#','.','.','.','.','.'],
	    ['.','.','#','#','.' ,'.', '.'],
	    ['#','.','#','E','.','#','.']]


print(shortestPath(0,0,grid))
