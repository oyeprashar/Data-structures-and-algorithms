def getNthFromLast(head,n):
    
    ptr1 = head 
    ptr2 = head
    count = 1 
    
    while ptr2 != None and count != n:
        count += 1
        ptr2 = ptr2.next 
    
    if ptr2 == None:
        return -1
    
    while ptr2.next != None:
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    
    return ptr1.data