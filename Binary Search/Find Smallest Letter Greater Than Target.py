def binarySearch(left,right,arr,searchKey,ans):
	if left <= right:

		mid = (left + right) // 2

		if arr[mid] > searchKey:
			# we save this and move to left to minimize it 
			ans[0] = arr[mid]
			return binarySearch(left,mid-1,arr,searchKey,ans)

		else:
			# if char at mid is smaller than target we move to right to go to a bigger character
			return binarySearch(mid+1,right,arr,searchKey,ans)

def findNext(arr,char):
	searchKey = char
	left = 0
	right = len(arr) - 1
	ans = [arr[0]]

	binarySearch(left,right,arr,searchKey,ans)
	return ans[0]

arr1 = ["c", "f", "j"]
char1 = "a"

arr2 = ["e","e","e","e","e","e","n","n","n","n"]
char2 = "e"
print(findNext(arr1,char1))
print(findNext(arr2,char2))


