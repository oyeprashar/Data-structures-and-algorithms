class Solution:

    def detectLoop(self, head):

        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None and slow is not None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return fast, True

        return None, False

    def removeLoop(self, head):

        if head is None:
            return head

        nodeInLoop, isLoopPresent = self.detectLoop(head)

        if isLoopPresent is False:
            return head

        # case 1 : nodeInLoop.next is head
        if nodeInLoop.next is head:
            nodeInLoop.next = None
            return head

        # case 2 : nodeInLoop is head
        if nodeInLoop is head:
            curr = head
            while curr.next != head:
                curr = curr.next
            curr.next = None
            return head

        # case 3 : nodeInLoop is some generic node
        curr = head
        while curr.next != nodeInLoop.next:
            curr = curr.next
            nodeInLoop = nodeInLoop.next

        nodeInLoop.next = None
        return head
