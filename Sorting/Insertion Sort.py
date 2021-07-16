"""
==== ALGORITHM FOR INSERTION SORT ====	
>> for i in range(1,len(arr))
	-> key = arr[i]; j = i - 1;

	>> while j is greator than equal to zero and key is smaller than element at j:
		-> copy element at index j to index j + 1
		-> decrement j by 1

	-> since we are out of the loop it means that key is not smaller than element at j 
	   and element at j + 1 is a duplicate, so we copy key to index j + 1

Time Complexity: Worst case => O(n2) | Average case => O(n2) | Best case => O(n) | Space Complexity = O(1) | Inplace Sorting = YES | Stable = YES
"""
def insertionSort(arr):

	for i in range(1,len(arr)):
		key = arr[i]

		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1

		arr[j+1] = key
	return arr

arr = [12,11,13,5,6]
print(insertionSort(arr))
























