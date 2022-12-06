def findingSquareRootHelper(l,r,arr,ans,target):
	if l<=r:
		mid = (l + r) // 2

		if arr[mid]*arr[mid] <= target:
			#update ans and move right to see if any other better answer exists
			ans[0] = mid
			return findingSquareRootHelper(mid+1,r,arr,ans,target)

		else:
			# agar arr[mid]*arr[mid] > target
			# move left to find smaller value
			return findingSquareRootHelper(l,mid-1,arr,ans,target)


def findSquareRoot(target):
	arr = [x for x in range(target + 1)]
	ans = [-1]
	l = 0
	r = len(arr) - 1
	findingSquareRootHelper(l,r,arr,ans,target)
	return ans[0]


print(findSquareRoot(9))

