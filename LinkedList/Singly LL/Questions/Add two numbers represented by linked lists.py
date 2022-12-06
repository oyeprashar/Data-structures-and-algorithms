class Solution:
    
    def addTwoLists(self, first, second):
        
        # step1 : reverse both the linkedlists
        prev = None
        curr = first
        head1 = None
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        head1 = prev
        
        prev = None
        curr = second
        head2 = None
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        head2 = prev
        
        curr1 = head1
        curr2 = head2
        left = 0
        prev = None
        finalHead = None
        
        while curr1 != None or curr2 != None:
            
            if curr1 == None:
                num1 = 0
            else:
                num1 = curr1.data
            
            if curr2 == None:
                num2 = 0
            else:
                num2 = curr2.data
            
            currSum = num1 + num2 + left
            
            if currSum % 10 == currSum:
                left = 0 
                newData = currSum
            else:
                newData = currSum % 10
                left = int((currSum/10)%10)
            
            newNode = Node(newData)
            if prev == None:
                finalHead = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode
            
            if curr1 != None:
                curr1 = curr1.next
            if curr2 != None:
                curr2 = curr2.next
            
        # print("left =",left)
        # Reverse this LinkedList
        
        if left == 1:
            prev.next = Node(1)
        
        prev = None
        curr = finalHead
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev
                