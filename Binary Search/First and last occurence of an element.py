def firstOccurenceHelper(l,r,arr,key,ans):
	mid = (l+r) // 2

	if l>= r:
		return 

	if arr[mid] == key:
		ans[0] = mid
		return firstOccurenceHelper(l,mid-1,arr,key,ans)

	elif key < arr[mid]:
		return firstOccurenceHelper(l,mid-1,arr,key,ans)

	else:
		return firstOccurenceHelper(mid+1,r,arr,key,ans)


def lastOccurenceHelper(l,r,arr,key,ans):

	mid = (l+r) // 2

	if l>=r:
		return 

	if arr[mid] == key:
		ans[0] = mid
		return lastOccurenceHelper(mid+1,r,arr,key,ans)

	elif key < arr[mid]:
		return lastOccurenceHelper(l,mid-1,arr,key,ans)
	else:
		return lastOccurenceHelper(mid+1,r,arr,key,ans)

def lastOccurence(arr,key):
	ans =[3 ** 38]
	l = 0
	r = len(arr) - 1
	lastOccurenceHelper(l,r,arr,key,ans)
	return ans[0]


def firstOccurence(arr,key):
	ans = [3 ** 38] * 1
	l = 0
	r = len(arr) - 1
	firstOccurenceHelper(l,r,arr,key,ans)
	return ans[0]

arr = [1,2,3,8,8,8,8,8,10,12,15,20]
print("First occurence of 8 is at index ",firstOccurence(arr,8))
print("Last occurence of 8 is at index ",lastOccurence(arr,8))
