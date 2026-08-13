class Solution:
    def isSubset(self, arr1, arr2):
        # is arr2 a subset of arr1?

        freq1 = {}
        for element in arr1:
            if element in freq1:
                freq1[element] += 1
            else:
                freq1[element] = 1

        freq2 = {}
        for element in arr2:
            if element in freq2:
                freq2[element]  += 1
            else:
                freq2[element] = 1


        for key in freq2:
            if key not in freq1 or freq2[key] > freq1[key]:
                return False

        return True
