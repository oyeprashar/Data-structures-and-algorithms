class Solution:
    def kthElement(self, arr1, arr2, k):

        i = j = 0
        count = 0

        while i < len(arr1) and j < len(arr2):

            count += 1
            current = None

            if arr1[i] < arr2[j]:
                current = arr1[i]
                i += 1

            else:
                current = arr2[j]
                j += 1

            if count == k:
                return current

        while i < len(arr1):
            count += 1
            if count == k:
                return arr1[i]
            i += 1

        while j < len(arr2):
            count += 1
            if count == k:
                return arr2[j]
            j += 1
