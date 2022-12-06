# TIME COMPLEXITY : O(n^2 * n) = O(n^3) | SPACE COMPLEXITY = O(n)
def getFactorial(num,DP):
	if num == 0 or num == 1:
		return 1

	if DP[num] != -1:
		return DP[num]

	DP[num] = num * getFactorial(num-1,DP)

	return DP[num]

def factorial(num):
	DP = [-1] * (num+1)
	DP[0] = 1
	DP[1] = 1
	return getFactorial(num,DP)

def numOfBT(N):

	memory = [0] * (N + 1)
	memory[0] = 1
	memory[1] = 1

	for x in range(2,N+1):
		ans = 0
		for i in range(1,x+1):
			ans += memory[i-1]*memory[x-i]*factorial(x)

		memory[x] = ans

	return memory[N]


print(numOfBT(2))
