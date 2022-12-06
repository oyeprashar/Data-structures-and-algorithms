def rodCutting(prices):
    memory = [0] * (len(prices) + 1)

    for i in range(len(prices)):
        currLen = i + 1

        ans = -3 ** 38
        for j in range(len(prices)):
            cutLen = j + 1
            if currLen - cutLen >= 0:
                res = prices[j] + memory[currLen - cutLen]
                ans = max(ans, res)

        memory[currLen] = ans

    return memory


prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
prices2 = [3, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(prices1))
print(rodCutting(prices2))