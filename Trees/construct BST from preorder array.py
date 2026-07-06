"""
Input: arr[] = [40, 30, 35, 80, 100]
Output: [35, 30, 100, 80, 40]

Explanation: PreOrder: 40 30 35 80 100
"""

INT_MIN = -3**38
INT_MAX = 3**38

class Solution:

    def constructTree(self, currIndex, preorderArray, minValue, maxValue):

        if currIndex[0] >= len(preorderArray):
            return None
            
        currValue = preorderArray[currIndex[0]]

        if currValue < minValue or currValue > maxValue:
            return None

        currNode = Node(currValue)
        currIndex[0] += 1

        currNode.left = self.constructTree(currIndex, preorderArray, minValue, currNode.data)
        currNode.right = self.constructTree(currIndex, preorderArray, currNode.data, maxValue)

        return currNode


    def preToBST(self, preorderArray):
        currIndex = [0]
        root = self.constructTree(currIndex, preorderArray, minValue = INT_MIN, maxValue = INT_MAX)
        return root
