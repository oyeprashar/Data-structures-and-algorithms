"""
>> The problem with infinite array is where to put the right pointer?
>> The idea to solve this problem is to initialize left = 0 and right =1 a
>> Both these pointers will grow if element we are trying to find is not in this range
>> if element is not in this range, left = right and right = 2 * right
"""

def binarySearch(left,right,arr,key):
	if left <= right:
		mid = (left + right) // 2

		if key == arr[mid]:
			return mid
		elif key > arr[mid]:
			# move to the right
			return binarySearch(mid+1,right,arr,key)
		else:
			# move to the left
			return binarySearch(left,mid-1,arr,key)
	else:
		return -1

def growingThePointers(arr,key):
	left = 0
	right = 1
	ans = binarySearch(left,right,arr,key)
	while ans == -1:
		left = right
		right *= 2

		ans = binarySearch(left,right,arr,key)
	return ans

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,"INF_DONT_ACCESS"]
key = 29

print(growingThePointers(arr,key))