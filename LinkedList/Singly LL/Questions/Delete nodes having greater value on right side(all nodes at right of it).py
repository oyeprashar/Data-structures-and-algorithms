class Solution:
    def compute(self,head):
        
        # step 1 : reverse the linkedlist
        curr = head
        prev = None
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        #step 2 : maintain and update a max and use to to remove nodes
        newHead = prev
        max1 = prev.data 
        prevValid = prev
        
        curr = newHead
        
        while curr != None:
            
            if curr.data >= max1:
                max1 = curr.data
                prevValid = curr
                curr = curr.next
            
            else:
                prevValid.next = curr.next
                curr = curr.next
        
        curr = newHead
        prev = None
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev