def segZeroes(leftPtr,rightPtr,arr):
	while leftPtr <= rightPtr:

		if arr[leftPtr] == 0 and arr[rightPtr] == 0:
			leftPtr += 1

		elif arr[leftPtr] == 1 and arr[rightPtr] == 1:
			rightPtr -= 1

		elif arr[leftPtr] == 1 and arr[rightPtr] == 0:
			# swap
			arr[leftPtr] = 0
			arr[rightPtr] = 1

			leftPtr += 1
			rightPtr -= 1

		elif arr[leftPtr] == 0 and arr[rightPtr] == 1:
			leftPtr += 1
			rightPtr -= 1
	

	return arr

def segregate(arr):
	leftPtr = 0
	rightPtr = len(arr) - 1

	return segZeroes(leftPtr,rightPtr,arr)


arr = [0,1,0,0,1,0,1,1,0]
arr1 = [1,1,0,0,0,1,1,0,0,0,1]
arr2 = [0, 1, 0, 1, 1, 1]
arr3 = [ 0, 1, 0, 1, 1, 1 ]

print(segregate(arr))
print(segregate(arr1))
print(segregate(arr2))
print(segregate(arr3 ))