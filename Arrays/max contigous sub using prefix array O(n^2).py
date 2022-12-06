def maxContigousSum(array):
    # convert array into prefix sum array
    prev = array[0]
    for i in range(1,len(array)):
        array[i] += prev
        prev = array[i]

    maxSum = -3**38
    for i in range(1,len(array)-1):
        for j in range(i,len(array)):
            if i == 0:
                currSum = array[j]
            else:
                currSum = array[j] - array[i-1]
            
            if currSum > maxSum:
                maxSum = currSum

    return max(maxSum, max(array))


array1 = [-1,-2,-3,-4]
array2 = [1, 2, 3, -2, 5]
array3 = [2, -3, 4, -1, -2, 1, 5, -3]

print(maxContigousSum(array3))
