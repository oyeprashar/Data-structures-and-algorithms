"""
Just use the two pointer technique like used in finding intersection between two sorted arrays
"""
def findIntersection(head1,head2):
    curr1 = head1
    curr2 = head2
    prev = None
    head = None
    
    while curr1 != None and curr2 != None:
        
        if curr1.data == curr2.data:
            newNode = Node(curr1.data)
            
            if prev == None:
                head = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        elif curr1.data < curr2.data:
            curr1 = curr1.next
        
        elif curr2.data < curr1.data:
            curr2 = curr2.next
        
    return head