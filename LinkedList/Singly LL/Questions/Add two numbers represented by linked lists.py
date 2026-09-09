class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def removeLeadingZeroes(self, head):

        if head is not None and head.next is None and head.data == 0:
            return head

        while head is not None:

            if head.data == 0:
                head = head.next
            else:
                return head

        return None

    def reverse(self, head):

        prev = None
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def addTwoLists(self, head1, head2):
        reversedHead1 = self.reverse(head1)
        reversedHead2 = self.reverse(head2)

        curr1, curr2 = reversedHead1, reversedHead2
        carry = 0

        """
        345
         21
        """
        newHead = None
        lastNode = None

        while curr1 is not None or curr2 is not None:

            num1 = 0
            num2 = 0

            if curr1 is not None:
                num1 = curr1.data
                curr1 = curr1.next

            if curr2 is not None:
                num2 = curr2.data
                curr2 = curr2.next

            total = num1 + num2 + carry # even tho either of the num can be None but there still be some carry

            if total <= 9:
                currData = total
                carry = 0
                pass
            else:
                currData = total % 10
                carry = total // 10

            newNode = Node(currData)

            if newHead is None:
                newHead = newNode
            else:
                lastNode.next = newNode

            lastNode = newNode

        if carry > 0:
            lastNode.next = Node(carry)
            lastNode = lastNode.next

        newHead = self.reverse(newHead)
        return self.removeLeadingZeroes(newHead)