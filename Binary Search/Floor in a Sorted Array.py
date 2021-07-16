"""
What is floor?
Given a sorted array and a value x, the floor of x is the largest element in 
array smaller than or equal to x. Write efficient functions to find floor of x.
"""

def binarySearch(left,right,arr,value,ans):
	if left <= right:
		mid = (left + right) // 2

		if arr[mid] <= value:
			# save this and move right to maximize it 	
			ans[0] = arr[mid]
			return binarySearch(mid+1,right,arr,value,ans)

		else:
			# else the current element is bigger than value, so we move to left
			return binarySearch(left,mid-1,arr,value,ans)
	else:
		return -1

def getFloor(arr,value):
	left = 0 
	right = len(arr) - 1
	ans = [-1]
	binarySearch(left,right,arr,value,ans)
	return ans[0]

arr1 = [1, 2, 8, 10, 10, 12, 19]
value1 = 5
arr2 = [1, 2, 8, 10, 10, 12, 19] 
value2  = 20
arr3 = [1, 2, 8, 10, 10, 12, 19]
value3 = 0
print(getFloor(arr1,value1))