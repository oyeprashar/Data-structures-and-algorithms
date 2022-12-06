def maxLen(n, arr):
    
    prefixSum = 0
    occurrence = {}
    
    maxLen = 0
    
    for i in range(len(arr)):
        prefixSum += arr[i]
        
        if prefixSum == 0:
            maxLen = max(i+1,maxLen)
        
        elif prefixSum in occurrence:
            oldIndex = occurrence[prefixSum]
            maxLen = max(maxLen,i-oldIndex)
            
        else:
            occurrence[prefixSum] = i
        
    return maxLen