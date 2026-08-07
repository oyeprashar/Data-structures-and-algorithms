class Solution:

    def findUnion(self, arr1, arr2):

        arr1.sort()
        arr2.sort()

        i = 0
        j = 0
        res = []

        while i < len(arr1) and j < len(arr2):


            if arr1[i] <= arr2[j]:
                elementToAdd = arr1[i]
                i += 1

            else:
                elementToAdd = arr2[j]
                j += 1

            if len(res) == 0 or elementToAdd != res[-1]:
                res.append(elementToAdd)

        while i < len(arr1):

            if arr1[i] != res[-1]:
                res.append(arr1[i])
            i += 1

        while j < len(arr2):

            if arr2[j] != res[-1]:
                res.append(arr2[j])
            j += 1

        return res
