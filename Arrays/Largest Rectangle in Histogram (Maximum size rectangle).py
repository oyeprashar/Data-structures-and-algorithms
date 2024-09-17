INT_MIN = -3**38

class Solution:


    def getLeftLimit(self, arr):

        leftLimit = [0] * len(arr)
        stack = [] # [(index, value)]

        for i in range(len(arr)):

            # pop all the non blocking element
            while len(stack) > 0 and stack[-1][1] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                leftLimit[i] = 0

            # blocking element found
            elif stack[-1][1] < arr[i]:
                leftLimit[i] = stack[-1][0] + 1

            stack.append([i, arr[i]])

        return leftLimit 


    def getRightLimit(self, arr):
        rightLimit = [0] * len(arr)
        stack = [] # [(index, value)]

        for i in range(len(arr) - 1, -1, -1):

            # remove all the non blocking elements from the stack
            while len(stack) > 0 and stack[-1][1] >= arr[i]:
                stack.pop()

            # extreme right limit is len(arr) - 1 i.e. the last index
            if len(stack) == 0:
                rightLimit[i] = len(arr) - 1

            # blocking element
            elif stack[-1][1] < arr[i]:
                rightLimit[i] = stack[-1][0] - 1

            stack.append([i, arr[i]])

        return rightLimit

    def getMaxArea(self,histogram):

        leftLimit = self.getLeftLimit(histogram)
        rightLimit = self.getRightLimit(histogram)

        maxArea = INT_MIN

        for i in range(len(arr)):
            width = rightLimit[i] - leftLimit[i] + 1
            currArea = histogram[i] * width
            maxArea = max(maxArea, currArea)

        return maxArea
