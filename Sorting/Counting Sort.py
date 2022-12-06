"""
==== ALGORITHM FOR COUNTING SORT ====	
>> Find out the max element in the array
>> Create a array named count with len = max element + 1, initialized with 0 at all indices
>> Loop thro the input array and store the frequency in the count array, use element as the index to access the count array
>> Convert the count array into a cummulative sum array
>> The index in the count is element and the value is not their postion in the sorted array (not index, they are position)
>> Now iterate the input array from last to first index
>> Use the element to access the count array
>> Decrement the value in the count array by 1 and this is the index in the sorted array
>> Place the element at that index in the ans array

Time Complexity: Worst case => O(n+k)| Average case => O(n+k) |Best case => O(n+k) |Space Complexity = O(n+k) |Inplace Sorting = NO| Stable = YES 
"""

def countingSort(arr):
	# arr must be from index 0 to k where k is the highest element
	k = max(arr)
	count = [0] * (k + 1)

	for num in arr:
		count[num] += 1

	# making count cummulative sum of its elements,
	# cummulative array will contain the postion of each element(postion starts from 1, if we subtract 1 we wil get their index)
	prev = count[0]

	for i in range(1,len(count)):
		count[i] = count[i] + prev
		prev = count[i]


	ans = [-1] * len(arr)

	curr = len(arr) - 1

	while curr != -1:
		element = arr[curr]	# get the element from the orignal unsorted array
		count[element] -= 1	# decrement it by one because it was postion and subtracting one will give its index
		itsIndex = count[element] # count counts their index
		ans[itsIndex] = element # put the element at its correct index in the ans array

		curr -= 1 # move to left to other element in the array

	return ans

arr = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(countingSort(arr))























