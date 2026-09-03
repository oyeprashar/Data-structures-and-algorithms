
"""
- The approach is to keep all the smaller elements in arr1 and bigger elements in the arr2
- Since both arrays are sorted, we do not have to process all the elements
- We simply put a pointer on the biggest element of arr1 and smallest element of arr2 and while elements in arr1 are
    bigger than elements in arr2, we keep on swapping them
- After this loop exists, all the bigger elements are in arr2
- Sort arr1 and arr2
"""


class Solution:
    def mergeArrays(self, arr1, arr2):

        i = len(arr1) - 1 # biggest element of arr1
        j = 0 # smallest element of arr2

        while i >= 0 and j < len(arr2) and arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1

        arr1.sort()
        arr2.sort()

        return arr1, arr2
