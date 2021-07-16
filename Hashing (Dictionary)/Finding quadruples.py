def fourSum(arr, k):
    if len(arr) == 0:
        return arr
    arr = sorted(arr)
    n = len(arr)
    ans = []
    # finding two nos first

    for i in range(n-3):
        for j in range(i+1,n-2):

            leftPtr = j + 1
            rightPtr = n - 1

            while leftPtr < rightPtr:
                if arr[leftPtr] + arr[rightPtr] + arr[i] + arr[j] == k:
                    currSet = set()
                    currSet.add(i)
                    currSet.add(j)
                    currSet.add(leftPtr)
                    currSet.add(rightPtr)
                    
                    if len(currSet) == 4:
                        item = [arr[leftPtr],arr[rightPtr],arr[i],arr[j]]
                        item = sorted(item)
                        ans.append(item)
                        
                    leftPtr += 1
                    rightPtr -= 1

                elif arr[leftPtr] + arr[rightPtr] + arr[i] + arr[j] < k:
                    # agar we need to increase the sum we increase left ptr and rightPtr is already
                    # at the high end since array is sorted
                    leftPtr +=1
                else:
                    # matlab sum required se badha h toh rightPrt will be reduced
                    rightPtr -= 1
                    
    # LOGIC TO REMOVE DUPLICATE LISTS
    ans = sorted(ans)
    n = len(ans) - 1

    while n > 0:
    
        if ans[n] == ans[n-1]:
            ans.pop(n)
        n -= 1
  

    return ans