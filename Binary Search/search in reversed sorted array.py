def binarySearchHelper(left,right,arr,key):
	if left <= right:

		mid = (left + right) // 2

		if arr[mid] == key:
			return mid

		elif key > arr[mid]:
			# since the array is reversed after sorting, to find bigger element than mid we move to left
			return binarySearchHelper(left,mid-1,arr,key)

		else:
			return binarySearchHelper(mid+1,right,arr,key)

	else:
		return -1
def binarySearch(arr,key):
	left = 0
	right = len(arr) - 1
	return binarySearchHelper(left,right,arr,key)

arr = [5, 4, 3, 2, 1]
key = 4
print(binarySearch(arr,key))


