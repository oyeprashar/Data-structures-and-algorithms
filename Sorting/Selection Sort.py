"""
==== ALGORITHM FOR SELECTION SORT ====	
Two nested loops are used. Outter loops goes from index 0 to second last index, inner loop goes from index 1 to last index
>> outter loop
   -> Set minIndex to the index outter loop is currently at
   	  >> Inner loop
   	     -> form the index outter loop is currently at till the last index, find the smallest element smaller than minIndex
   	  -> outside swap element at index i with the new element at minIndex	

Time Complexity: Worst case => O(n2) | Average case => O(n2) | Best case => O(n2) | Space Complexity = O(1) | Inplace Sorting = YES | Stable = NO
"""
def selectionSort(arr):
	for i in range(len(arr)-1):
		minIndex = i

		for j in range(i+1,len(arr)):

			if arr[j] < arr[minIndex]:
				minIndex = j
		
		arr[i],arr[minIndex] = arr[minIndex],arr[i]

	return arr

arr = [99,88,77,66,55,44,22,11]
arr2 = [1,2,3,4,5,6,7,8,9]

print(selectionSort(arr)) 
print(selectionSort(arr2))

