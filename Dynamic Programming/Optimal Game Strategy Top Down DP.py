# TIME COMPLEXITY = O(N^2) | SPACE COMPLEXITY = = O(N^2)

def optimalStrategy(i,j,arr,memory):
	if i > j:
		return 0

	if memory[i][j] != -1:
		return memory[i][j]

	op1 = arr[i] + min(optimalStrategy(i+2,j,arr,memory),optimalStrategy(i+1,j-1,arr,memory))
	op2 = arr[j] + min(optimalStrategy(i+1,j-1,arr,memory),optimalStrategy(i,j-2,arr,memory))

	ans = max(op1,op2)
	memory[i][j] = ans

	return ans

def getOptimalAns(arr):
	memory = []
	for x in range(len(arr)):
		list1 = []
		for y in range(len(arr)):
			list1.append(-1)
		memory.append(list1)

	i = 0; j = len(arr)-1;
	return optimalStrategy(i,j,arr,memory)

arr = [5,3,7,10]
print(getOptimalAns(arr))