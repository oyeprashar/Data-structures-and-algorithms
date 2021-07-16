# TIME COMPLEXITY = O(N^2) | SPACE COMPLEXITY = = O(N^2)
def uniqueWays(i, j, matrix, res, desti, destj, memory):
    if i < 0 or i < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return 0

    if matrix[i][j] == 1:
        return 0

    if memory[i][j] != -1:
        return memory[i][j] % 1000000007

    if i == desti and j == destj:
        res += 1
        return res

    ans = uniqueWays(i, j + 1, matrix, res, desti, destj, memory) + uniqueWays(i + 1, j, matrix, res, desti, destj,memory)

    memory[i][j] = ans
    return ans


p, q, n = map(int, input().split())
matrix = []
for u in range(p + 1):
    list1 = []
    for v in range(q + 1):
        list1.append(0)
    matrix.append(list1)

for i in range(n):
    x1, x2 = map(int, input().split())
    matrix[x1][x2] = 1

i = j = 1
desti = len(matrix) - 1
destj = len(matrix[0]) - 1
memory = []
for x in range(len(matrix)):
    list1 = []
    for y in range(len(matrix[0])):
        list1.append(-1)
    memory.append(list1)

res = 0
if matrix[1][1] == 1:
    print(0)
else:
    ans = uniqueWays(i, j, matrix, res, desti, destj, memory)
    print(ans)

