def findElement(arr,n):
    
    leftArr = [0] * len(arr)
    leftArr[0] = arr[0]
    
    for i in range(1,len(arr)):
        
        leftArr[i] = max(leftArr[i-1],arr[i])
    
    rightArr = [0] * len(arr)
    rightArr[-1] = arr[-1]
    
    for j in range(len(arr)-2,-1,-1):
        rightArr[j] = min(rightArr[j+1],arr[j])
        
    
    for k in range(1,len(arr)-1):
        
        if arr[k] >= leftArr[k-1] and arr[k] <= rightArr[k+1]:
            return arr[k]
        
    return -1