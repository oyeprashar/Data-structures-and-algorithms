"""
finding aisa element in sorted array jisska difference with the key is the least
arr = [1,3,8,10,15]
key = 12 

logic: the difference between the key and the largest number in arr smaller than the key (floor) would be least 
	   of the difference betweent the key the smallest number greator than the key (ceil)


"""

def floor(left,right,arr,key,floorAns):
	if left <= right:

		mid = (left + right) // 2

		if arr[mid] <= key:
			floorAns[0] = arr[mid]
			return floor(mid+1,right,arr,key,floorAns)

		else:
			# else move left to find a number smaller than key
			return floor(left,mid-1,arr,key,floorAns)

def ceil(left,right,arr,key,ceilAns):
	if left <= right:
		mid = (left + right) // 2

		if arr[mid] >= key:
			# save the ans and we move left to minimize it!
			ceilAns[0] = arr[mid]
			return ceil(left,mid-1,arr,key,ceilAns)
		else:
			# we move right to find an element greator than key
			return ceil(mid+1,right,arr,key,ceilAns)

def minDifference(arr,key):
	left = 0
	right = len(arr) - 1
	floorAns = [0]
	ceilAns = [0]
	floor(left,right,arr,key,floorAns)
	ceil(left,right,arr,key,ceilAns)

	if floorAns[0] > key:
		ans1 = floorAns[0] - key
	else:
		ans1 = key - floorAns[0]

	if ceilAns[0] > key:
		ans2 = ceilAns[0] - key	
	else:
		ans2 = key - ceilAns[0]

	if ans1 < ans2:
		return ans1
	else:
		return ans2

arr = [1,3,8,10,12,15]
key = 12 
print(minDifference(arr,key))