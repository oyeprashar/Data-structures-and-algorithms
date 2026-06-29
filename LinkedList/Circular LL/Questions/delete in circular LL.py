'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    def deleteNode(self, head, key):
    
        if head is None:
            return head

        # deleting the head
        if head.data == key:

            # head is the only node in the linkedin list
            if head.next == head:
                return None

            # make the last node point to head.next and move head to head.next
            oldHead = head
            head = head.next

            curr = head
            while curr.next != oldHead:
                curr = curr.next

            curr.next = head
            return head

        curr = head

        # find the node before the target node and make it point to point next to the target
        while True:

            if curr.next.data == key:
                curr.next = curr.next.next
                return head

            curr = curr.next

            # we were not able to find the target node and again came back to the head 
            if curr == head:
                return head
