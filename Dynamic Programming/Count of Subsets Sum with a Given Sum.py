def numberOfSubsetHelper(i, arr, target, memory):
    if i == len(arr) and target != 0:
        return 0

    if target == 0:
        return 1

    if memory[i][target] != -1:
        return memory[i][target]

    memory[i][target] = numberOfSubsetHelper(i + 1, arr, target - arr[i], memory) + numberOfSubsetHelper(i + 1, arr, target, memory)
    return memory[i][target]

def numberOfSubset(arr, target):
    i = 0
    memory = []
    for x in range(len(arr) + 1):
        list1 = []
        for y in range(target + 1):
            list1.append(-1)
        memory.append(list1)

    return numberOfSubsetHelper(i, arr, target, memory)


# arr1 = [1, 2, 3, 3]
# target1 = 6
#
# arr2 = [1,2,1]
# target2 = 3
#
# arr3 = [3,3,3,3]
# target3 = 6

arr1 = [1,1,1,1,1]
target1 = 3
print(numberOfSubset(arr1, target1))
# print(numberOfSubset(arr2, target2))
# print(numberOfSubset(arr3, target3))
