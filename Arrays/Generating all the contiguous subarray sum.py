"""
==== Generating all the contiguous subarray sum ====
"""

def generate(arr):
    ans = []
    # we convert the arr into prefix sum array and now it will contain sum from index 0 to current index
    prev = arr[0]
    for x in range(1,len(arr)):
        arr[x] += prev
        prev = arr[x]

    ans.extend(arr)

    for i in range(1,len(arr)): # we are starting from 1 because 0 ke saaare sums we already know because of our prefix sum array
        for j in range(i,len(arr)): # jth loop starts from i because we consider a case when we dont add any element to i and consider the element itself
                                    # so when i == j and we do arr[j] -arr[i-1] arr[i] is found
            currSum = arr[j] - arr[i-1]
            ans.append(currSum)

    return ans

arr = [3,2,1,0]
print(generate(arr))
