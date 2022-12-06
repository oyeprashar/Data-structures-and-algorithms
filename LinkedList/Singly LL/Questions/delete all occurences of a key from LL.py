def deleteAllOccurances(head, x):
    curr = head 
    prev = None 

    while curr != None:
        
        if curr.data == x:
            if prev == None:
                head = curr.next 
                
            else:
                prev.next = curr.next

            curr = curr.next
                
        else:
            prev = curr
            curr = curr.next
        
    return head