class Solution:

    def findSumLongestPath(self, root, currSum, currLength, maxLen, res):

        if root is None:
            return

        # when we have reached a leaf node, we check and safe the longest path answer!
        if root.left is None and root.right is None:
            currSum += root.data

            # longest path? This is the answer
            if currLength > maxLen[0]:
                res[0] = currSum
                maxLen[0] = currLength

            # another equally long path? The max sum is the answer
            elif currLength == maxLen[0]:
                res[0] = max(res[0], currSum)

            return

        self.findSumLongestPath(root.left, currSum + root.data, currLength + 1, maxLen, res)
        self.findSumLongestPath(root.right, currSum + root.data, currLength + 1, maxLen, res)

    def sumOfLongRootToLeafPath(self, root):

        maxLen = [-3**38]
        res = [-1]
        self.findSumLongestPath(root, 0, 0, maxLen, res)
        return res[0]
