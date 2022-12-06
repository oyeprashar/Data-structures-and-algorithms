# this is kadane's algorithm
import sys
arr = [-2,-3,4,-1,-2,1,5,-3]
def arr_conti_sum(arr):
	max_ending_here = 0
	max_so_far = -sys.maxsize - 1
	for i in range(len(arr)):
		max_ending_here = max_ending_here + arr[i]
		if max_ending_here < arr[i]:
			max_ending_here = arr[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
	return max_so_far

print(arr_conti_sum(arr))

