"""
Suppose there is an array from 1 to N, given a subset we need to find the missing number and the repeating number

==== LOGIC ===
-> generate a dictionary with all elements of the array
-> now start traversing from range 1 till N 
    -> if the element is not in the dictinary, append it to the missing array
    -> if the element is having frequency more than once then append it to repeating array
-> return repeating.extended(missing)
"""

class Solution:
    def findTwoElement(self, arr):

        """
        Duplicate element is the one where the index is already marked, and we find the element again
        Missing element is the one where the index is not marked at all

        """

        missingElements = []
        duplicateElements = []

        # logic to find out the duplicate elements
        for num in arr:
            num = abs(num)
            if arr[num - 1] < 0:
                duplicateElements.append(num)
            else:
                arr[num - 1] *= -1


        for num in range(1, len(arr) + 1):

            if arr[num -1] > 0:
                missingElements.append(num)

        res = []
        res.extend(duplicateElements)
        res.extend(missingElements)
        return res
