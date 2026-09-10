class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
This is a circular linkedlist where the last node is connected with the head
"""

class Solution:

    def getNodeBeforeTarget(self, head, target):

        curr = head

        # [MOST Important] : since this is a circular linked list. There will be no none limiting it!
        while curr.next is not head:
            if curr.next.data == target:
                return curr
            curr = curr.next

        return None


    def deleteNode(self, head, key):

        # case 1 : head
        if head.data == key:

            curr = head
            while curr.next is not head:
                curr = curr.next

            curr.next = head.next
            head = head.next
            return head

        nodeBeforeTarget = self.getNodeBeforeTarget(head, key)

        if nodeBeforeTarget is None:
            return head

        # case 2 : last node
        if nodeBeforeTarget.next.next == head:
            nodeBeforeTarget.next = head
            return head

        # case 3 : some generic node between head and last
        nodeBeforeTarget.next = nodeBeforeTarget.next.next
        return head
