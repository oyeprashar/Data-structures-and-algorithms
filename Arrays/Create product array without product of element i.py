"""
Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]


At index i, we want product[i - 1] * product[i + 1]
"""


class Solution:

    def getLeftProductArr(self, arr):

        leftProductArr = [1] * len(arr)
        leftProductArr[0] = arr[0]
        for i in range(1, len(arr)):
            leftProductArr[i] = leftProductArr[i - 1] * arr[i]

        return leftProductArr

    def getRightProductArr(self, arr):

        rightProductArr = [1] * len(arr)
        rightProductArr[-1] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            rightProductArr[i] = rightProductArr[i + 1] * arr[i]

        return rightProductArr

    def productExceptSelf(self, arr):

        leftArr = self.getLeftProductArr(arr)
        rightArr = self.getRightProductArr(arr)
        res = []
        for i in range(len(arr)):

            if i == 0:
                res.append(rightArr[1])

            elif i == len(arr) - 1:
                res.append(leftArr[len(arr) - 2])

            else:
                res.append( leftArr[i-1] * rightArr[i + 1] )

        return res





s = Solution()
print(s.productExceptSelf([10, 3, 5, 6, 2]))
