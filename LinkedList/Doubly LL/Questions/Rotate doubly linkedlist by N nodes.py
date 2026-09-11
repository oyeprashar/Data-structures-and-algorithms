class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Solution:

    def getLength(self, head):

        count = 0
        curr = head

        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def rotateDLL(self, head, k):

        if head is None:
            return None

        length = self.getLength(head)
        effectiveRotations = k % length

        if effectiveRotations == 0:
            return head

        count = 1
        curr = head
        while curr is not None and count != effectiveRotations:
            curr = curr.next
            count += 1

        newHead = curr.next
        curr.next = None
        newHead.prev = None

        curr = newHead
        while curr.next != None:
            curr = curr.next
        #
        curr.next = head
        head.prev = curr

        return newHead
