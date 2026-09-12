class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


class Solution:

    def merge(self, head1, head2):
        curr1 = head1
        curr2 = head2

        newHead = None
        lastNode = None

        while curr1 is not None and curr2 is not None:

            currData = None

            if curr1.data < curr2.data:
                currData = curr1.data
                curr1 = curr1.bottom
            else:
                currData = curr2.data
                curr2 = curr2.bottom

            newNode = Node(currData)

            if newHead is None:
                newHead = newNode
            else:
                lastNode.bottom = newNode

            lastNode = newNode

        while curr1 is not None:
            lastNode.bottom = Node(curr1.data)
            lastNode = lastNode.bottom
            curr1 = curr1.bottom

        while curr2 is not None:
            lastNode.bottom = Node(curr2.data)
            lastNode = lastNode.bottom
            curr2 = curr2.bottom

        return newHead


    def flatten(self, head):

        # we cannot process the last column linkedlist
        if head is None or head.next is None:
            return head

        # second last and last is merged and we come back to left side
        head.next = self.flatten(head.next)
        return self.merge(head, head.next)
