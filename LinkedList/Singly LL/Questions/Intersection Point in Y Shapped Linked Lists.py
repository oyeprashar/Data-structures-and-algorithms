def intersetPoint(head1,head2):
    # step1 : count the len of head1 and head2
    
    curr1 = head1
    curr2 = head2
    count1 = 0
    count2 = 0
    
    while curr1 != None:
        count1 += 1
        curr1 = curr1.next
    
    while curr2 != None:
        count2 += 1
        curr2 = curr2.next
        
    if count1 == count2:
        curr1 = head1
        curr2 = head2
        
        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1.data
            curr1 = curr1.next
            curr2 = curr2.next
        
    elif  count2 < count1:
        target = abs(count1-count2)
        currCount = 0
        while head1 != None and currCount != target:
            currCount += 1
            head1 = head1.next
        

        curr1 = head1
        curr2 = head2
        
        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1.data
            curr1 = curr1.next
            curr2 = curr2.next
    
    elif count1 < count2:
        target = abs(count1-count2) 
        currCount = 0
        while head2 != None and currCount != target:
            currCount += 1
            head2 = head2.next
        

        curr1 = head1
        curr2 = head2
        
        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1.data
            curr1 = curr1.next
            curr2 = curr2.next
        