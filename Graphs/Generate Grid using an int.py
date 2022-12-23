"""
given an odd number generate the matrix

n = 3

   0 1 2
0 [X X X]
1 [X 3 X]
2 [2 1 4]

   0 1 2
0 [8 6 9]
1 [5 3 7]
2 [2 1 4]

Approach:
	We will be using BFS to generate this matrix
	We start from the last row (n-1) and mid col (n//2) then do a BFS from there
"""


def generateGrid(n):

	grid = []
	visited = []

	for i in range(n):
		currRow = []
		visitedRow = []
		for j in range(n):
			currRow.append(0)
			visitedRow.append(False)
		grid.append(currRow)
		visited.append(visitedRow)

	rowIndex = n - 1
	colIndex = n // 2
	queue = [[rowIndex, colIndex]]
	currNum = 1
	moves = [[0, -1], [-1, 0], [0, 1]]
	visited[rowIndex][colIndex] = True

	while len(queue) > 0:

		curr = queue.pop(0)
		grid[curr[0]][curr[1]] = currNum
		currNum += 1

		for move in moves:
			newi = curr[0] + move[0]
			newj = curr[1] + move[1]

			if newi >= 0 and newi < n and newj >= 0 and newj < n and visited[newi][newj] is False:
				queue.append([newi, newj])
				visited[newi][newj] = True

	for row in grid:
		print(row)


generateGrid(3)








