"""
Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x.
"""

def binarySearch(left,right,arr,value,ans):
	if left <= right:
		mid = (left + right) // 2

		if arr[mid] >= value:
			# we are finding ceil, it is smallest element greator/equal than x, so we move left to minize it
			# saving the value of mid
			ans[0] = arr[mid]
			return binarySearch(left,mid-1,arr,value,ans)

		else:
			# else we go to a greator element to compare it 
			return binarySearch(mid+1,right,arr,value,ans)

def getCeil(arr,x):
	left = 0
	right = len(arr) - 1
	ans = [-1]
	binarySearch(left,right,arr,x,ans)
	return ans[0]

arr = [1, 2, 8, 10, 10, 12, 19]
x1 = 0
x2 = 1
x3 = 5
x4 = 20
print(getCeil(arr,x1))
print(getCeil(arr,x2))
print(getCeil(arr,x3))
print(getCeil(arr,x4))