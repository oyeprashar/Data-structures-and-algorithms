class Solution:
    def splitList(self, head):
        #code here
        slow = head
        fast = head
        
        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = head
        
        curr = head2
        while curr.next != head:
            curr = curr.next
        curr.next = head2
    
        
        return head,head2