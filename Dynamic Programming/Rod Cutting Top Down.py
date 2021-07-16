# ==== TOP DOWN USING THE UNBOUNDED KNAPSACK ====
def maxProfit(i,n,priceArray,memory):
    if i == len(priceArray) and n == 0:
        return 0

    if i+1 > n:
        return 0

    return max(priceArray[i] + maxProfit(i,n-(i+1),priceArray,memory),maxProfit(i+1,n,priceArray,memory))


def getMaxProfit(N,priceArray):
    memory = []
    for x in range(len(priceArray)):
        list1 = []
        for y in range(N+1):
            list1.append(-1)
        memory.append(list1)

    i = 0
    return maxProfit(i,N,priceArray,memory)

priceArray = [1,5,8,9,10,17,17,20]
N = 8
print(getMaxProfit(N,priceArray))

# ANOTHER METHOD: CALLING ALL POSSIBLE CUTS AT EACH N

def maxProfit(N,prices,memory):
	if N == 0:
		return 0

	if memory[N] != -1:
		return memory[N]

	ans = -3**38
	for i in range(len(prices)):
		cutLen = i + 1
		currCut = N - cutLen
		if currCut >=0:
			res = prices[i] + maxProfit(N-cutLen,prices,memory)
			ans = max(res,ans)

	memory[N] = ans
	return	ans

def rodCutting(prices):
	N = len(prices)
	memory = [-1] * (len(prices)+1)
	return maxProfit(N,prices,memory)


prices1 =[1,5,8,9,10,17,17,20] #correct ouput is 22
prices2 = [3,5,8,9,10,17,17,20] #correct output is 24
print(rodCutting(prices1))
# print(rodCutting(prices2))
