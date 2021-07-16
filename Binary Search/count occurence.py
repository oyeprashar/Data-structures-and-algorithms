"""
Algo to count occurence

-> find the first occurence
-> find the last occurence 
-> return (last occurence - first occurence) + 1
"""

def firstOccurence(left,right,arr,key,firstAns):
	if left <= right:
		mid = (left + right) // 2

		if key == arr[mid]:
			# save the index
			firstAns[0] = mid
			# move to left to find the first time that element occurs
			return firstOccurence(left,mid-1,arr,key,firstAns)

		elif key > arr[mid]:
			# move to thr right is key is greator than the element at the mid
			return firstOccurence(mid+1,right,arr,key,firstAns)

		else:
			# move to the left if the key is less than mid
			return firstOccurence(left,mid-1,arr,key,firstAns)


def lastOccurence(left,right,arr,key,lastAns):
	if left <= right:
		mid = (left + right) // 2

		if key == arr[mid]:
			# save the index 
			lastAns[0] = mid
			# move to right to find the last occurence
			return lastOccurence(mid+1,right,arr,key,lastAns)

		elif key > arr[mid]:
			# move to right to find the correct element
			return lastOccurence(mid+1,right,arr,key,lastAns)

		else:
			# move to the left
			return lastOccurence(left,mid-1,arr,key,lastAns)

def countOccurence(arr,key):
	left = 0
	right = len(arr) - 1
	firstAns = [-1]
	lastAns = [-1]
	firstOccurence(left,right,arr,key,firstAns)
	lastOccurence(left,right,arr,key,lastAns)
	first = firstAns[0]
	last = lastAns[0]
	return (last - first) + 1

arr = [2,4,10,10,10,18,20,20]
key = 10
print(countOccurence(arr,key))