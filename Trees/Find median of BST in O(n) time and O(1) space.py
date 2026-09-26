"""
Why always our formula (count[0] + 1) // 2 works?


    What the question wants us to return?
        Even: return value at (n/2).
        Odd: return value at ((n+1)/2).

    Since we are counting the nodes, (count[0] + 1) // 2 just lands on the correct count!
"""




class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    def getTotalNode(self, root, count):

        if root is None:
            return

        self.getTotalNode(root.left, count)
        count[0] += 1
        self.getTotalNode(root.right, count)

    def getMiddleTwoNodes(self, root, targetcount, currCount, savedNodes):

        if root is None:
            return None

        self.getMiddleTwoNodes(root.left, targetcount, currCount, savedNodes)

        currCount[0] += 1

        if currCount[0] == targetcount:
            savedNodes[0] = root.data

        self.getMiddleTwoNodes(root.right, targetcount, currCount, savedNodes)

    def findMedian(self, root):

        count = [0]
        self.getTotalNode(root, count)
        savedNodes = [None]
        self.getMiddleTwoNodes(root, (count[0] + 1) // 2, [0], savedNodes)
        return savedNodes[0]
