"""
The logic is that if we do XOR of every element in the array then the pairs of same numbers cancells out and res would the number that occured only once
"""
arr = [1,2,3,4,9,4,3,1,2]

res = arr[0]
for i in range(1,len(arr)):
    res ^= arr[i]
print(res)