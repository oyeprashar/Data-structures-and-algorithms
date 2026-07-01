"""
*---------------------- Approach ----------------------*
original linked list
1 -> 2 -> 3 -> 4

after reversing
4 -> 3 -> 2 -> 1

- The old head becomes the last node
- The last processed nodes (prev) becomes new head
- nextNode pointer points to the next segment or None
"""

class Solution:

    def reverseKGroup(self, head, k):

        if head is None:
            return head

        count = 0 # no nodes reversed yet
        curr = head
        prev = None
        while curr is not None and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count += 1 # one node reversed so increment

        newHead = prev
        oldHead = head
        oldHead.next = self.reverseKGroup(nextNode, k)
        return newHead
