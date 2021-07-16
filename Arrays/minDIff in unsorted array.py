"""
NAIVE APPROACH O(n2)
compare all elements with all other elements and calculate the minimum difference

EFFICIENT APPROACH O(nlogn)
sorted the array and calculate difference between adjancent elements

Why adjacent elements?
Because arr is sorted and instead of comparing with all other elements we can just compare it with next element
ek element ko usske just bade element subtract karengye 

"""
arr = [1, 5, 3, 19, 18, 25]
sortedArr = sorted(arr)
minDiff = 3 ** 38
for i in range(len(sortedArr)-1):
    curr = sortedArr[ i + 1] - sortedArr[i]
    if curr < minDiff:
        minDiff = curr
print(minDiff)