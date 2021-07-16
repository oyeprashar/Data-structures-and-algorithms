#NOTE: The logic to determine the length of loop in LL is:
#           1) Identify the common node where two pointers will reach after some time
#           2) Count the length from this common point until the common point is encountered again
class Node():   

    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList():
   
    def __init__(self):
        self.head = None
    
    def loopLen(self):
        
        slow = self.head
        fast = self.head 
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                length = 1
                temp1  = fast.next
                while(temp1 != fast):
                    length = length + 1
                    temp1 = temp1.next
                return length             #NOTE: 11 -> 22 -> 33 -> back to head
            
        return "NO LOOP"                            
    
llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = llist.head

print(llist.loopLen())