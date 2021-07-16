# NOTE: Logic to split a circular linked list:
#          1) we have to find the  middle and the last node
#          2) then we have to store the next pointer of this middle and last node
#          3) then we have to change these ponters according to split the circular LinkedList

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None 
    
    def printList(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            slow = self.head
            fast = self.head
            while(fast != None):
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    temp1 = fast.next
                    while(temp1 != fast):
                        print(temp1.data)
                        temp1 = temp1.next
                    print(fast.data)
                    return
            return "No loop"
    def __len__(self):
        if self.head is None:
            return 0
        else:
            slow = self.head
            fast = self.head
            while(fast.next != None):
                slow = slow.next.next
                fast = fast.next.next
                if slow == fast:
                    length = 1
                    temp2 = fast.next
                    while(temp2 != fast):
                        length = length + 1
                        temp2 = temp2.next
                    return length
    def splitList(self):
        
        if len(self) % 2 == 0:
            
            mid = int(len(self)/2)
            temp3 = self.head
            for _ in range(mid-1):
                temp3 = temp3.next
            mid_node = temp3
            
            temp4 = self.head
            for _ in range(len(self)-1):
                temp4 = temp4.next
            last_node = temp4
            second_head = mid_node.next 

            mid_node.next = self.head
            last_node.next = second_head
           
            
            slow1 = self.head
            fast1 = self.head
            while(fast1 != None):
                slow1 = slow1.next
                fast1 = fast1.next.next
                if fast1 == slow1:
                    temp5 = fast1.next
                    print(fast1.data)
                    while(temp5!=fast1):
                        print(temp5.data) 
                        temp5 = temp5.next
                    
                    break 
            print() # prints a blank line
            slow2 = second_head
            fast2 = second_head
            while(fast2 != None):
                slow2 = slow2.next
                fast2 = fast2.next.next
                if slow2 == fast2:
                   
                    temp6 = fast2.next
                    print(fast2.data) 
                    while(temp6 != fast2):   
                        print(temp6.data) 
                        temp6 = temp6.next
                    
                    break
        
        else:
            mid = int(len(self)/2)
            temp3 = self.head
            for _ in range(mid):
                temp3 = temp3.next
            mid_node = temp3
            
            temp4 = self.head
            for _ in range(len(self)-1):
                temp4 = temp4.next
            last_node = temp4
            second_head = mid_node.next 

            mid_node.next = self.head
            last_node.next = second_head
           
            
            slow1 = self.head
            fast1 = self.head
            while(fast1 != None):
                slow1 = slow1.next
                fast1 = fast1.next.next
                if fast1 == slow1:
                    temp5 = fast1.next
                    print(fast1.data)
                    while(temp5!=fast1):
                        print(temp5.data) 
                        temp5 = temp5.next
                    
                    break 
            print() # prints a blank line
            slow2 = second_head
            fast2 = second_head
            while(fast2 != None):
                slow2 = slow2.next
                fast2 = fast2.next.next
                if slow2 == fast2:
                   
                    temp6 = fast2.next
                    print(fast2.data)
                    while(temp6 != fast2):   
                        print(temp6.data) 
                        temp6 = temp6.next
                     
                    break

llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fouth = Node(44)
fifth = Node(55)

llist.head.next = second
second.next = third
third.next = fouth
fouth.next = fifth
fifth.next = llist.head

llist.splitList()