
def numOfSets(i, currSetSum, totalSum, arr, setTarget, memory):
    if i == len(arr) and currSetSum == setTarget:
        return 1

    elif i == len(arr) and currSetSum != setTarget:
        return 0

    if memory[i][currSetSum] != -1:
        return memory[i][currSetSum]

    memory[i][currSetSum] = numOfSets(i + 1, currSetSum + arr[i], totalSum, arr, setTarget, memory) + numOfSets(i + 1, currSetSum,totalSum,arr,setTarget,memory)
    return memory[i][currSetSum]


def getRes(arr, t):
    sum1 = sum(arr)
    memory = []
    for x in range(len(arr)):
        list1 = []
        for y in range(sum1 + 1):
            list1.append(-1)
        memory.append(list1)

    totalSum = sum(arr)
    setTarget = (t + totalSum) / 2
    i = 0
    currSetSum = 0

    return numOfSets(i, currSetSum, totalSum, arr, setTarget, memory)


arr = [1, 1, 3, 2]
t = 1

print(getRes(arr, t))
