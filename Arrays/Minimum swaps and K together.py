def minSwap (arr, n, k) : 
    
    count = 0
    for num in arr:
        if num <= k:
            count += 1
            
    # print(count)
    
    i = 0
    j = count - 1
    minBad = 0
    
    # print(i,j)
    
    for x in range(i,j+1):
        if arr[x] > k:
            minBad += 1
            
    currBad = minBad
    
    # print(currBad)
    
    while j < len(arr) and i < len(arr):
        
        # print("----------------------")
        # print("i =",i,"j =",j,"currBad =",currBad)
        
        j += 1
        
        if j < len(arr):
            if arr[j] > k:
                currBad += 1
                
        if j == len(arr):
            break
            
        if arr[i] > k:
            currBad -= 1
            
        i += 1
        
        # print("i =",i,"j =",j,"currBad =",currBad)
        
        
        minBad = min(minBad,currBad)
    
    return minBad