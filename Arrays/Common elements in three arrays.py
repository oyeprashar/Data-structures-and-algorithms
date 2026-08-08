class Solution:

    def commonElements(self, arr1, arr2, arr3):

        i = j = k = 0
        commonElements = []
        arr1.sort()
        arr2.sort()
        arr3.sort()

        while i < len(arr1) and j < len(arr2) and k < len(arr3):

            if arr1[i] == arr2[j] == arr3[k]:
                commonElements.append(arr1[i])
                i += 1
                j += 1
                k += 1

            else:
                minElement = min(arr1[i], arr2[j], arr3[k])

                if minElement == arr1[i]:
                    i += 1

                elif minElement == arr2[j]:
                    j += 1

                else:
                    k += 1

        return  sorted(list(set(commonElements)))
