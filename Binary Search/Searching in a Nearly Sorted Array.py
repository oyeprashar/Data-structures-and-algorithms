"""
an at element at index i can be at index i-1 or i+1
so evertime we find the mid index we compare the key with i -1 and i + 1 

"""


def binarySearch(left,right,arr,key):
	if left <= right:

		mid = (left + right) // 2

		if key == arr[mid]:
			return mid

		elif arr[mid] < arr[right] and key == arr[mid+1]:
			return mid + 1

		elif arr[mid] > arr[left] and key == arr[mid - 1]:
			return mid - 1

		elif key > arr[mid]:
			return binarySearch(mid+2,right,arr,key)
		else:
			return binarySearch(left,mid-2,arr,key)

	else:
		return -1

def getIndex(arr,key):
	left = 0
	right = len(arr) - 1
	return binarySearch(left,right,arr,key)

arr = [5,10,20,30,40]
print(getIndex(arr,5))