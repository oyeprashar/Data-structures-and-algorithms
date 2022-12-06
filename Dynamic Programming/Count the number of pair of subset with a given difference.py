
def numOfSets(i, currSetSum, totalSum, arr, setTarget, memory):
    if currSetSum == setTarget:
        return 1

    elif i == len(arr):
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


arr1 = [1, 1, 3, 2]
t1 = 1


arr2 = [0,0,0,0,0,0,0,0,1]
t2 = 1

print(getRes(arr1, t1))
print(getRes(arr2, t2))