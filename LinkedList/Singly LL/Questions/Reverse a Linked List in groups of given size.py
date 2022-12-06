def reverse(head, k):
    curr = head
    prev = None
    count = 0
    
    while curr != None and count < k:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
        count += 1
    
    if nextNode != None:
        head.next = reverse(nextNode,k)
    
    return prev

