class Solution:
    
    def findMid(self,head):
    
        slow = head
        fast = head
        prevSlow = None
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            prevSlow = slow
            slow = slow.next
        
        return prevSlow

    def mergeSort(self, head):
        
        if head == None:
            return None
        
        if head.next == None:
            return head 
        
        mid = self.findMid(head)
        
        left = head
        right = mid.next 
        mid.next = None
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        # merge and create a new linked list
        prev = None
        head = None
        curr1 = left
        curr2 = right
        
        while curr1 != None and curr2 != None:
            
            if curr1.data < curr2.data:
                newNode = Node(curr1.data)
                curr1 = curr1.next
                
            else:
                newNode = Node(curr2.data)
                curr2 = curr2.next
            
            if head == None:
                head = newNode
                prev = newNode
            
            else:
                prev.next = newNode
                prev = newNode
        
        while curr1 != None:
            newNode = Node(curr1.data)
            if head == None:
                head = newNode
                prev = newNode
            
            else:
                prev.next = newNode
                prev = newNode
            curr1 = curr1.next
            
        while curr2 != None:
            newNode = Node(curr2.data)
            if head == None:
                head = newNode
                prev = newNode
            
            else:
                prev.next = newNode
                prev = newNode
            curr2 = curr2.next
            
        
        return head
        