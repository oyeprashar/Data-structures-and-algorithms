"""
ALGO:
-> Let us find if the array is ascending or descending by comparing first and the last element
-> Then apply binarySearch accordingly
"""
def binarySearchHelper(left,right,arr,key,ascending):
	if left <= right:

		mid = (left + right) // 2

		if arr[mid] == key:
			return mid

		elif key > arr[mid]:
			if ascending is True:
				# it means greator elements are on the right side so we move to right
				return binarySearchHelper(mid+1,right,arr,key,ascending)

			else:
				# for descending we move to left to find the greator elements
				return binarySearchHelper(left,mid-1,arr,key,ascending)
		else:
			# for ascending we move to left to find the smaller elements
			if ascending is True:
				return binarySearchHelper(left,mid-1,arr,key,ascending)
			else:
				# for descending we move to right to find the smaller elements
				return binarySearchHelper(mid+1,right,arr,key,ascending)

def binarySearch(arr,key):
	ascending = False
	if arr[-1] > arr[0]:
		ascending = True
	left = 0
	right = len(arr) - 1

	return binarySearchHelper(left,right,arr,key,ascending)

arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [9,8,7,6,5,4,3,2,1]
key = 9
print(binarySearch(arr1,key))
print(binarySearch(arr2,key))