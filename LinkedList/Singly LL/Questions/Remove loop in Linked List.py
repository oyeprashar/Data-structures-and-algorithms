class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        loopHai = False
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                loopHai = True
                break
            
        if loopHai == False:
            return head
            
        if slow == head:
            while slow.next != head:
                slow = slow.next
            slow.next = None
        
        else:
            slow = head
            while fast.next != slow.next:
                slow = slow.next
                fast = fast.next 
            fast.next = None
        
        return head