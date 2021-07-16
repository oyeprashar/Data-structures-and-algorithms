def findSubArrays(arr,n):
    sumArray = []
    sumArray.append(arr[0])
    
    for i in range(1,len(arr)):
        item = sumArray[-1] + arr[i]
        sumArray.append(item)
    
    dict1 ={}
    dict1[0] = 1
    ans = 0
    for num in sumArray:
        
        if num not in dict1:
            dict1[num] = 1
        else:
            print("for ",num," this is added to ans = ",dict1[num]," now ans is ",ans+dict1[num])
            ans += dict1[num]
            
            dict1[num] += 1
    print("total number of sub-arrays with sum zero = ",ans)
    return ans