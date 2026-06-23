class Solution:

    """
    Let's say we are at index i, and we want to compute the area. We need to find how much left area we can include?

    We start to travel to left from the index i and find a tower at index x whose height is less than i, we cannot this
    tower at index x because it is smaller than all the tower from i (move to left) till x + 1. So we compute area from
    x + 1 till index i.
    """
    def getLeftLimit(self, heights):

        leftArr = [0] * len(heights)
        stack = []

        for i in range(len(heights)):

            # If height of a tower is >= to current tower than i can include them
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()


            # no smaller element left of i
            if len(stack) == 0:
                leftArr[i] = 0

            # + 1 because the tower is smaller than towers between this and ith, so we cannot include this smaller
            # tower but include all the towers after it
            else:
                leftArr[i] = stack[-1] + 1

            stack.append(i)
        return leftArr

    def getRightLimit(self, heights):

        rightArr = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):

            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) == 0:
                rightArr[i] = len(heights) - 1
            else:
                rightArr[i] = stack[-1] - 1

            stack.append(i)

        return rightArr


    def largestRectangleArea(self, heights):

        leftLimits = self.getLeftLimit(heights)
        rightLimits = self.getRightLimit(heights)
        maxArea = 0

        # the loop runs from 0th till the last index because the tower itself can be the max Area
        for i in range(len(heights)):

            width = rightLimits[i] - leftLimits[i] + 1
            currentArea = width * heights[i]
            maxArea = max(maxArea, currentArea)

        return maxArea


s = Solution()
print(s.largestRectangleArea(heights = [2,1,5,6,2,3,1]))
