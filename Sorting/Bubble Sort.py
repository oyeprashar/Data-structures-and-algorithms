"""
==== ALGO FOR BUBBLE SORT ====
>> Outer loop goes from 0 till end of the array
>> For each value of outter loop, inner loop goes from 0 till n-i-1
>> If arr[j] > arr[j+1] then we swap them

How to detect that the array is already sorted and in this case how to reduce the time complexity to O(N)?
>> If in the first pass (0 to end of array), no swaps are made it means the array is already sorted and we break the outer loop
>> If in the first pass variable isAlreadySorted changes to False then bubble sort works normally!

Time Complexity: Worst case => O(n2) | Average case => O(n2) | Best case => O(n) | Space Complexity = O(1) | Inplace Sorting = YES  | Stable = YES
"""
def bubbleSort(arr):
	isAlreadySorted = True

	for i in range(len(arr)):
		print(i)

		for j in range(len(arr)-i-1):

			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				isAlreadySorted = False
		

		if isAlreadySorted is True:
			break
			

	return arr
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [64,34,25,12,22,11,90]
print(bubbleSort(arr2))
print(bubbleSort(arr1))