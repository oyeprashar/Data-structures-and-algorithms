def generateSubset(start,subset,target,ans,arr):

    if sum(subset) == target:
        s1 = subset.copy()
        ans.append(s1)
        return 

    if sum(subset) > target:
        return

    for i in range(start,len(arr)):                 # we first generate all the combinations including the element sitting at start index
        subset.append(arr[i])                       
        generateSubset(i,subset,target,ans,arr)
        subset.pop()

def combinationalSum(arr,target):       
    arr = sorted(list(set(arr)))            # set is used to remove the duplicates
    subset = []                             # sorted is used because generated subsets should be sorted
    ans = []
    generateSubset(0,subset,target,ans,arr)
    return ans 

arr = [7,2,6,5]
target = 16
print(combinationalSum(arr,target))