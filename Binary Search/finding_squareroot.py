def binarySearch(left, right, key, ans):

	if left <= right:

		mid = (left + right) // 2

		if mid * mid <= key:
			ans[0] = mid  # index represents the element
			# we move to right to maximize the answer
			binarySearch(mid + 1, right, key, ans)

		else:
			binarySearch(left, mid - 1, key, ans)


def findSqrt(num):

	ans = [None]
	binarySearch(0, num, num, ans)
	return ans[0]


print(findSqrt(125))


