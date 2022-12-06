"""
==== ALGO ===
>> Using the two pointer method to put a pointer at the start of the loop
>> Start traversing from this point we just found and count the number of nodes

"""
def countNodesinLoop(head):
   
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            break
        
    if fast == None or fast.next == None:
        return 0
        
    count = 1
    curr = slow.next
    
    while curr != slow:
        count += 1
        curr = curr.next
        
    return count
    