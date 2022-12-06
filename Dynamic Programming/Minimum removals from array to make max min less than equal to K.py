def minCount(left,right,k,arr,memory):

    if arr[right] - arr[left] <= k:
        return 0

    if left >= right:
        return 3**38

    if memory[left][right] != -1: 
        return memory[left][right]
    
    # moving to right
    op1 = 1 + minCount(left+1,right,k,arr,memory)

    # moving to left 
    op2 = 1 + minCount(left,right-1,k,arr,memory)


    memory[left][right] = min(op1,op2)
    return memory[left][right]

def getRes(arr,k):

    memory = []
    for x in range(len(arr)):
        list1 = []
        for y in range(len(arr)):
            list1.append(-1)
        memory.append(list1)

    arr.sort()
    return minCount(0,len(arr)-1,k,arr,memory)

arr = [1, 3, 4, 9, 10, 11, 12, 17, 20]  
k = 4
print(getRes(arr,k))

arr = [1, 5, 6, 2, 8]  
k = 2
print(getRes(arr,k))