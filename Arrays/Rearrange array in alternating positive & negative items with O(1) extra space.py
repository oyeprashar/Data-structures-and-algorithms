def rearrange(arr):

	arr.sort()
	i = j = 1

	while j < len(arr):

		if arr[j] >= 0:
			break 
		j += 1
	
	while arr[i] < 0 and j < len(arr):
		# since array is sorted, if arr[i] >= 0 then element after it would also be postive
		arr[i],arr[j] = arr[j],arr[i]
		i += 2
		j += 1
	
	return arr

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(rearrange(arr))