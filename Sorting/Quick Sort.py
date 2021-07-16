"""
==== ALGORITHM FOR QUICK SORT ====	
The main logic is that in each recursive call we bring the pivot element i.e. left most element to its correct postion and then recursively 
call the function for its left and right side.

We do this till we have atleast two elements 

Time Complexity: Worst case => O(n2)| Average case => O(nlogn) |Best case => O(nlogn) |Space Complexity = O(logn) |Inplace Sorting = YES| Stable = No
"""
def partition(arr,left,right):

	i = left + 1
	pivot = arr[left]
	for j in range(left + 1,right+1):

		if arr[j] <= pivot:
			arr[i],arr[j] = arr[j],arr[i]
			i += 1

	arr[left],arr[i-1] = arr[i-1],arr[left]

	return i - 1

def quickSort(arr,left,right):
	if left < right: # we run the function only when there are two or more element also only when the indices are also VALID!
					# because ek element me partition nhi ho payegi
	
		pivot = partition(arr,left,right)

		quickSort(arr,left,pivot-1) # pivot ke aage piche 
		quickSort(arr,pivot+1,right)# pivot element ko include nhi krna


arr = [77,88,99,66,11,99]
quickSort(arr,0,len(arr)-1)
print(arr)