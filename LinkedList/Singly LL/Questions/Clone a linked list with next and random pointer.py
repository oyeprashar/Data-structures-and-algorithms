class Solution:
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head == None:
            return None
        
        curr = head 
        
        while curr != None:
            # print(curr.val)
            nextNode = curr.next
            newNode = Node(curr.val)
            curr.next = newNode
            newNode.next = nextNode
            curr = nextNode
        
        # we have to use another loop to copy the random pointers because a random pointer might be pointing to elements backwards and
        # when we break the links between old and new linkedlist we cannot access the random ke copies, hence we have to copy the random
        # pointers in a seperate loop
        curr = head
        while curr!= None:
            if curr.random != None:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            
            curr = curr.next.next
        
        curr1 = head
        head2 = curr1.next
        curr2 = head2
        
        while curr1 != None and curr2 != None:
            
            curr1.next = curr1.next.next
            curr1 = curr1.next
            
            if curr2.next == None:
                curr2 = None
            else:
                curr2.next = curr2.next.next
                curr2 = curr2.next
        
            
        return head2