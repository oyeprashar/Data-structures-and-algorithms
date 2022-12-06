"""
==== ALGORITHM FOR HEAP SORT ====	
>> Build heap

>> Heap sort
   -> While last != -1 
   -> swap element at index 0 with last element
   -> decrement last by 1
   -> heapify index 0 with updated last

Time Complexity: Worst case => O(nlogn)| Average case => O(nlogn) |Best case => O(nlogn) |Space Complexity = O(1) |Inplace Sorting = YES| Stable = No 
"""


def heapify(currIndex,arr,last):		# max heap to get ascending order waali sorting
	newIndex = currIndex
	# last = len(arr)-1
	left = 2*currIndex
	right = 2*currIndex+1

	if left <= last and arr[left] > arr[newIndex]:
		newIndex = left

	if right <= last and arr[right] > arr[newIndex]:
		newIndex = right


	if newIndex != currIndex:
		#swap
		arr[newIndex],arr[currIndex] = arr[currIndex],arr[newIndex]

		# now our element is at newIndex and we need to again heapify the array
		heapify(newIndex,arr,last)

def convert2Heap(arr):
	lastNonLeaf = len(arr) // 2
	last = len(arr) - 1
	curr = lastNonLeaf

	while curr != -1:
		heapify(curr,arr,last)
		curr -= 1

def heapSort(arr):
	"""
	-> Convert it into a heap
	-> while last != -1
	-> swap element at index 0 with last
	-> last -= 1
	-> heapify from index 0 with this updated last
	"""
	convert2Heap(arr)
	last = len(arr) - 1

	while last != -1:
		#swap index 0 and last
		arr[0],arr[last] = arr[last],arr[0]
		last -= 1

		heapify(0,arr,last)





arr = [11,0,99,88,-1,77]
heapSort(arr)
print(arr)