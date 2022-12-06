arr = [1,2,4,8]
arr = [1,2,3,4,5]

def maxabsDiff(arr):
	arr.sort()
	i = 0
	j = len(arr)-1

	ans = []

	while i < j:
		ans.append(arr[i])
		ans.append(arr[j])
		i += 1
		j -= 1

	if len(arr) & 1 == 1:
		mid = len(arr) // 2 
		ans.append(arr[mid])

	ansSum = 0
	for i in range(len(ans)-1):
		ansSum += abs(ans[i]-ans[i+1])

	ansSum += abs(ans[0]-ans[-1])

	return ansSum

arr1 = [1,2,4,8]
arr2 = [1,2,3,4,5]

print(maxabsDiff(arr1))
print(maxabsDiff(arr2))