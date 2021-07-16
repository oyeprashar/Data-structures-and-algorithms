"""
Top down DP = recursion + memoisation
i.e. check kro kya yeh saved h already?
agar saved hai toh use kro saved ans warna toh compute kro aur save kro
TIME COMPLEXITY = O(N) | SPACE COMPLEXITY = O(N)

"""


def fib(n, ansDict):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    if ansDict[n] != -1:
        return ansDict[n]

    else:
        ansDict[n] = fib(n - 1, ansDict) + fib(n - 2, ansDict)

    return ansDict[n]


n = 125
ansDict = [-1] * (n + 1)
print(fib(n, ansDict))