"""
Given an array of size n, find all elements in array that appear more than n/k times. 
For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output 
should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements 
that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3. 
"""

def find(arr,k):
	target = len(arr) // k 

	freq = {}
	for num in arr:

		if num in freq:
			freq[num] += 1
		
		else:
			freq[num] = 1

	ans = []
	for num in freq:
		if freq[num] > target:
			ans.append((num,freq[num]))
		
	return ans 

print("First Test")
arr1 = [4, 5, 6, 7, 8, 4, 4]
size = len(arr1)
k = 3
print(find(arr1, k))

print("Second Test")
arr2 = [4, 2, 2, 7]
size = len(arr2)
k = 3
print(find(arr2, k))

print("Third Test")
arr3 = [2, 7, 2]
size = len(arr3)
k = 2
print(find(arr3, k))

print("Fourth Test")
arr4 = [2, 3, 3, 2]
size = len(arr4)
k = 3
print(find(arr4, k))


