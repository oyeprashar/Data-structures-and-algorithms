def getMinCoin(N,coinList,memory):
    if N == 0:
        return 0

    if memory[N] != 0:
        return memory[N]

    ans = 3**38
    for coin in coinList:
        x = N - coin

        if x >= 0:
            curr = getMinCoin(x,coinList,memory) + 1
            ans = min(curr,ans)

    memory[N] = ans
    return ans

def minCoin(N,coinList):
    memory = [0] * (N+1)

    getMinCoin(N,coinList,memory)
    print(memory)
    return memory[N]


N = 15
coinList = [1,7,10]
print(minCoin(N,coinList))