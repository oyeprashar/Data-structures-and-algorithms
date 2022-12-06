def findMaxSum(currIndex,arr,memory):

     if currIndex >= len(arr):
          return 0 

     if memory[currIndex] != -1:
          return memory[currIndex]
     
     op1 = 0
     if currIndex + 1 < len(arr):
          op1 = arr[currIndex] + arr[currIndex+1] + findMaxSum(currIndex+3,arr,memory)
     
     op2 = arr[currIndex] + findMaxSum(currIndex+2,arr,memory)

     op3 = findMaxSum(currIndex+1,arr,memory)

     memory[currIndex] = max(op1,op2,op3)

     return memory[currIndex]

def getMaxSum(arr):
     memory = [-1] * len(arr)
     return  findMaxSum(0,arr,memory)

arr1 = [1, 2, 3]
arr2 = [3000, 2000, 1000, 3, 10]
arr3 = [100, 1000, 100, 1000, 1]
arr4 = [1, 1, 1, 1, 1]
arr5 = [1, 2, 3, 4, 5, 6, 7, 8]

print(getMaxSum(arr1))
print(getMaxSum(arr2))
print(getMaxSum(arr3))
print(getMaxSum(arr4))
print(getMaxSum(arr5))
