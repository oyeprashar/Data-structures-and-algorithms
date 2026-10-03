class Solution:

    def maxSum(self, arr):
        newArr = []
        arr.sort()

        i = 0
        j = len(arr) - 1

        while i < j:
            newArr.append(arr[i])
            newArr.append(arr[j])
            i += 1
            j -= 1

        # if the len if odd, we will miss the middle element
        if len(arr) % 2 == 1:
            newArr.append(arr[len(arr)//2])

        total = 0
        for i in range(len(newArr) - 1):
            total += abs(newArr[i] - newArr[i + 1])

        total += abs(newArr[0] - newArr[-1])

        return total