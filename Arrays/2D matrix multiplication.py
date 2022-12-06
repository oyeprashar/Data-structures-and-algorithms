# Matrix multiplication

def multiply(mat1,mat2):
	sum1 = 0
	row1 = len(mat1)
	col1 = len(mat1[0])

	row2 = len(mat2)
	col2 = len(mat2[0])

	ans = []
	for x in range(row1):
		list1 = []
		for y in range(col2):
			list1.append(0)
		ans.append(list1)


	for i in range(row1):
		for j in range(col2):
			for k in range(row2):
				sum1 += mat1[i][k] * mat2[k][j]

			ans[i][j] = sum1
			sum1 = 0 

	return ans

# First matrix. M is a list
M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
 
# Second matrix. N is a list
N = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

mat1 = [[7, 8], [2 , 9]]
mat2 = [[14, 5], [5, 18]]
print(multiply(M,N))

# Output: 
# C[][] = {{188, 359}, {73, 172}}