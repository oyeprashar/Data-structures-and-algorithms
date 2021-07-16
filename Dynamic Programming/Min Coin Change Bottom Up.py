"""
<== This is bottom up approach ==> 
TIME COMPLEXITY = O(N*M) | SPACE COMPLEXITY = O(N)
"""

def minCoinsHelper(N,coinList):

	memory = [0] * (N+1)

	for i in range(1,N+1):
		ans = 3**38

		for coin in coinList:
			x = i - coin

			if x >= 0:
				curr = memory[x]

				if curr < ans:
					ans = curr

		memory[i] = ans + 1

	print(memory)
	return memory[N]

# N = 15
# coinList = [1,3,7,10]
N = 4
coinList = [1,2,3]
print(minCoinsHelper(N,coinList))