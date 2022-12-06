def findMinSize(arr,target):

    start = 0
    end = 0 
    count = 0
    minCount = 3**38
    currSum = 0

    while not(currSum <= target and end == len(arr)):

        if currSum <= target:
            currSum += arr[end]
            end += 1
            count += 1
        
        elif currSum > target:
            minCount = min(minCount,count)
            currSum -= arr[start]
            start += 1
            count -= 1

    if minCount == 3**38:
        return -1
    return minCount 


arr = [1,4,45,6,0,19]
target = 51
print(findMinSize(arr,target))

arr = [1, 10, 5, 2, 7]
target  = 9
print(findMinSize(arr,target))

arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
target = 280
print(findMinSize(arr,target))

arr = [1, 2, 4]
target = 8
print(findMinSize(arr,target))