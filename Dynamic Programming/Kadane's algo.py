class Solution:

    def maxSubArraySum(self, a, size):
        maxSum = a[0]
        curr = a[0]

        for i in range(1, len(a)):
            if curr + a[i] < a[i]:
                curr = a[i]

            else:
                curr += a[i]

            if curr > maxSum:
                maxSum = curr

        return maxSum
