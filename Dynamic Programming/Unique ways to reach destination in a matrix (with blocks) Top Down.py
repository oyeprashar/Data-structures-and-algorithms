def uniqueWays(i,j,matrix,res,desti,destj,memory):

	if i < 0 or i < 0 or i >= len(matrix) or j >= len(matrix[0]):
		return 0

	if matrix[i][j] == 1:
		return 0

	if memory[i][j] != -1:
		return memory[i][j] 

	if i == desti and j == destj:
		res += 1
		return res

	ans = uniqueWays(i,j+1,matrix,res,desti,destj,memory) +uniqueWays(i+1,j,matrix,res,desti,destj,memory)

	memory[i][j] = ans
	return ans


def getRes(matrix):
	i = j = 0
	desti = len(matrix)-1
	destj = len(matrix[0])-1
	memory = []
	for x in range(len(matrix)):
		list1 = []
		for y in range(len(matrix[0])):
			list1.append(-1)
		memory.append(list1)
		
	res = 0
	return uniqueWays(i,j,matrix,res,desti,destj,memory)
	

matrix = [[0,0,0],
		  [0,1,0],
		  [0,0,0]]


print(getRes(matrix))