class Solution:

    def moveHead(self, head, targetCount):

        if targetCount == 0:
            return head

        count = 0
        while head is not None and count != targetCount:
            count += 1
            head = head.next

        return head

    def getLength(self, head):

        count = 0
        curr = head

        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def intersectPoint(self, head1, head2):

        length1 = self.getLength(head1)
        length2 = self.getLength(head2)

        diff = abs(length1 - length2)

        # we need to move the head of the longer linkedList
        if length1 > length2:
            head1 = self.moveHead(head1, diff)
        else:
            head2 = self.moveHead(head2, diff)

        # keep moving the pointers unless the next node points to the same address
        while head1.next != head2.next:
            head1 = head1.next
            head2 - head2.next

        return head1.next
