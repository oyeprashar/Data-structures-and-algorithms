"""
Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]

Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3].
Since, we need to start with the positive integer first and then negative integer and so on
(by maintaining the relative order as well), hence we will take 9 from the positive set of elements
and then -2 after that 4 and then -1 and so on.
"""


class Solution:

    def rearrange(self, arr):

        positive_elements  = []
        negative_elements = []

        for num in arr:
            if num >= 0:
                positive_elements.append(num)
            else:
                negative_elements.append(num)

        flag = 0
        curr_index = 0
        i = 0
        j = 0

        while i < len(positive_elements) and j < len(negative_elements):

            if flag % 2 == 0:
                arr[curr_index] =  positive_elements[i]
                i += 1
            else:
                arr[curr_index] = negative_elements[j]
                j += 1

            flag += 1
            curr_index += 1

        # append any left positive elements
        while i < len(positive_elements):
            arr[curr_index] = positive_elements[i]
            i += 1
            curr_index += 1

        while j < len(negative_elements):
            arr[curr_index] = negative_elements[j]
            j += 1
            curr_index += 1

        return arr

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
s = Solution()
print(s.rearrange(arr))
