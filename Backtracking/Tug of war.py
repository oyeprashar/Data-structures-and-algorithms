"""
==== TUG OF WAR ====
We have to divide the elements into two arrays such that their absolute difference is minimum
if len(arr) is even, each array can have len(arr) / 2 elements
if len(arr) is odd, one array can have (len(arr) + 1) / 2 element and other (len(arr) - 1) / 2

so in each case we have say that one of the array will have (len(arr) + 1) // 2 elements

if n = 5(odd) -> (5+1) // 2 == 3
if n = 4(even) ->(4+1) // 2 = 2 
"""

def tugofwarHelper(index,subset1,subset2,arr,ans,capacity): 

    if index == len(arr):
        diff = abs(sum(subset1)-sum(subset2))
        min1 = ans[2]

        if diff < min1:
            ans[0] = subset1.copy()
            ans[1] = subset2.copy()
            ans[2] = diff

        
        return

    if len(subset1) < capacity:
        subset1.append(arr[index])
        tugofwarHelper(index+1,subset1,subset2,arr,ans,capacity)
        subset1.pop()    # this is useful because we want to add the element to subset2
        
    if len(subset2) < capacity:
        subset2.append(arr[index])
        tugofwarHelper(index+1,subset1,subset2,arr,ans,capacity)
        subset2.pop()   # this is useful because we want to backtrack
    
def tugofwar(arr):
    index = 0
    subset1 = []
    subset2 = []
    ans = [-1,-1,3**38]
    capacity = (len(arr) + 1) // 2
    tugofwarHelper(index,subset1,subset2,arr,ans,capacity)
    return ans

arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4] 
print(tugofwar(arr))
