

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:

    def getLastNode(self, head):

        curr = head
        while curr.next is not None:
            curr = curr.next

        return curr


    def givenSumPairs(self, head, target):

        leftNode = head
        rightNode = self.getLastNode(head)
        res = []

        while leftNode != rightNode:

            currSum = leftNode.data + rightNode.data

            if currSum == target:
                res.append([leftNode.data. rightNode.data])
                leftNode = leftNode.next
                rightNode = rightNode.prev

            elif currSum < target:
                leftNode = leftNode.next

            else:
                rightNode = rightNode.prev

        return res



