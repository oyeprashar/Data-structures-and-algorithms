"""
ALGORITHM
>> Get index of any 1 in the array by growing the left and right and using binary search, name it indexOfAny1
>> Now find first occurence of 1 in with left = 0 and right = indexOfAny1
"""
def firstOccurence(left,right,arr,indexOfAny1,ans):
	if left <= right:
		mid = (left + right) // 2

		if arr[mid] == 1:
			# save the index and move to left
			ans[0] = mid
			return firstOccurence(left,mid-1,arr,indexOfAny1,ans)
		else:
			# move to right to find 1 since array is sorted 1s are on the right
			return firstOccurence(mid+1,right,arr,indexOfAny1,ans)

def binarySearch(left,right,arr,key):
	if left <= right:
		mid = (left + right) // 2

		if key == arr[mid]:
			return key
		elif key > arr[mid]:
			# move to right
			return binarySearch(mid+1,right,arr,key)
		else:
			# move to left
			return binarySearch(left,mid-1,arr,key)
	else:
		return -1

def getFirst1(arr):
	left = 0
	right = 1
	key = 1
	indexOfAny1 = binarySearch(left,right,arr,key)

	while indexOfAny1 == -1:
		left = right
		right *= 2

		indexOfAny1 = binarySearch(left,right,arr,key)
	ans = [-1]
	firstOccurence(left,right,arr,indexOfAny1,ans)
	return ans[0]

arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(getFirst1(arr))