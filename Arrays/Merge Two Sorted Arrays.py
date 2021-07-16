def mergeArrays(arr1,arr2,i,j,ans):
	if i > len(arr1)-1 and j > len(arr2)-1:
		return # do nothing

	if i < len(arr1) and j < len(arr2):

		if arr1[i] < arr2[j]:

			ans.append(arr1[i])
			return mergeArrays(arr1,arr2,i+1,j,ans)
		else:

			ans.append(arr2[j])
			return mergeArrays(arr1,arr2,i,j+1,ans)

	elif i < len(arr1) and j > len(arr2)-1:
		ans.append(arr1[i])
		return mergeArrays(arr1,arr2,i+1,j,ans)

	elif j < len(arr2) and i > len(arr1)-1:
		ans.append(arr2[j])
		return mergeArrays(arr1,arr2,i,j+1,ans)




arr2 = [1,2,3,4,5,6,7,8,9]
arr1 = [10,11,12]
ans = []
mergeArrays(arr1,arr2,0,0,ans)
print(ans)