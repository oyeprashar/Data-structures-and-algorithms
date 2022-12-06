def knapsack01(currIndex,target,arr,memory):

    if target == 0:
        return 1

    if currIndex >= len(arr):
        return 0
    
    if target - arr[currIndex] < 0:
        return knapsack01(currIndex+1,target,arr,memory)
    
    if memory[currIndex][target] != -1:
        return memory[currIndex][target]
    
    op1 = knapsack01(currIndex+1,target,arr,memory)
    op2 = knapsack01(currIndex+1,target-arr[currIndex],arr,memory)

    memory[currIndex][target] = op1 + op2

    return memory[currIndex][target]

def countSubsets(arr,target):
    memory = []
    for x in range(len(arr)+1):
        list1 = []
        for y in range(target+1):
            list1.append(-1)
        memory.append(list1)
    
    return knapsack01(0,target,arr,memory)
