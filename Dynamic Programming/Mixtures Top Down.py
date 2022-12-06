# TIME COMPLEXITY = O(N^3) | SPACE COMPLEXITY = O(N)
def mixtures(L,R,array,memory):

	if L == R:
		return 0

	if memory[L][R] != -1:
		return memory[L][R]

	ans = 3**38
	for k in range(L,R): # R is not included 
		leftSol = sum(array[L:k+1]) % 100
		rightSol = sum(array[k+1:R+1]) % 100

		currSmoke = mixtures(L,k,array,memory) + mixtures(k+1,R,array,memory) + leftSol*rightSol
		ans = min(ans,currSmoke)

	memory[L][R] = ans

	return ans


def getRes(array):
	memory = []
	for x in range(len(array)):
		list1 = []
		for y in range(len(array)):
			list1.append(-1)
		memory.append(list1)

	L = 0
	R = len(array)-1
	return mixtures(L,R,array,memory)


array = [40,60,20]
print(getRes(array))