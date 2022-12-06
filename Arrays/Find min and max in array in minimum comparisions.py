"""
find the max and min in minimum comparisions
"""

def find(left,right,arr):

	if left == right:
		return arr[left],arr[left]
	
	if right == left + 1:
		currMax = None
		currMin = None 

		if arr[0] > arr[1]:
			currMax = arr[0]
			currMin = arr[1]
		else:
			currMax = arr[1]
			currMin = arr[0]

			return currMax,currMin


	mid = (left+right) // 2

	leftMax,leftMin = find(left,mid,arr)
	rightMax,rightMin = find(mid+1,right,arr)

	return max(leftMax,rightMax), min(leftMin,rightMin)

def getMaxMin(arr):
	return find(0,len(arr)-1,arr)

arr = [1000, 11, 445, 1, 330, 3000]
print(getMaxMin(arr))


	

	
