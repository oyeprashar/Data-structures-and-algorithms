def MCM(L,R,array,memory):

	# if we have just one array mxn then multiplcations done is zero
	if R == L+1:
		return 0

	if memory[L][R] != -1:
		return memory[L][R]

	ans = 3 ** 38

	for k in range(L+1,R):
		# multiplcations done to form the left half + right half + inndo halves ko multiply krne me jitne operations lagega
		op1 = MCM(L,k,array,memory)
		op2 = MCM(k,R,array,memory)
		curr = array[L] * array[k] * array[R]

		res = op1 + op2 + curr
		ans = min(ans,res)

	memory[L][R] = memory

	return ans

def getMCM(array):
	
	# creating memory matrix 
	memory = []
	for x in range(len(array)):
		list1 = []
		for y in range(len(array)):
			list1.append(-1)
		memory.append(list1)

	L = 0
	R = len(array)-1
	return MCM(L,R,array,memory)

array = [10, 30, 5, 60]
print(getMCM(array))