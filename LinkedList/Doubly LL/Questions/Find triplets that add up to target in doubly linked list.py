class linkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:

    def getLastNode(self, head):

        curr = head
        while curr.next is not None:
            curr = curr.next

        return curr

    def getTriplets(self, head, target):

        if head is None or head.next is None:
            return None

        lastNode = self.getLastNode(head)
        curr = head
        res = []

        while curr.next.next is not None:

            leftNode = curr.next
            rightNode = lastNode

            while leftNode != rightNode and leftNode.prev != rightNode:

                currSum = leftNode.data + rightNode.data + curr.data

                if currSum == target:
                    res.append([leftNode.data, rightNode.data, curr.data])
                    leftNode = leftNode.next
                    rightNode = rightNode.prev

                elif currSum < target:
                    leftNode = leftNode.next

                else:
                    rightNode = rightNode.prev

            curr = curr.next

        return res
