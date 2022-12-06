"""
Two moves are allowed
1) right
2) down
"""
def minCost(mat):

	memory = []
	for x in range(len(mat)):
		list1 = []
		for y in range(len(mat[0])):
			list1.append(0)
		memory.append(list1)

	memory[0][0] = mat[0][0]

	# filling the first row
	for j in range(1,len(memory[0])):
		memory[0][j] = mat[0][j] + memory[0][j-1]

	# filling the first column
	for i in range(1,len(memory)):
		memory[i][0] = mat[i][0] + memory[i-1][0]

	# filling other cells now
	for x in range(1,len(memory)):
		for y in range(1,len(memory[0])):
			memory[x][y] = min(memory[x-1][y],memory[x][y-1]) + mat[x][y]

	return memory[len(memory)-1][len(memory[0])-1]

mat = [[2,8,4,1,6,4,2],
	   [6,0,9,5,3,8,5],
	   [1,4,3,4,0,6,5],
	   [6,4,7,2,4,6,1],
	   [1,0,3,7,1,2,7],
	   [1,5,3,2,3,0,9],
	   [2,2,5,1,9,8,2]]

print(minCost(mat))