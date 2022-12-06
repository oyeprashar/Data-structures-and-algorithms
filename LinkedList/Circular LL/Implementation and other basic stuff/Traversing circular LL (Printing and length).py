#NOTE: Steps to traverse a Circular LinkedList
#       1) first use two pointers to find a node where these two pointers will meet
#       2) then start traversing the circular linkedlist from this node and stop when we encounter this node again

# We will implement traversing and print the circular linkedlist

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head is None:
            print("The Circular LinkedList is empty")    
        else:
            slow = self.head
            fast = self.head
            while(fast.next != None):
                slow = slow.next
                fast =fast.next.next
                if slow == fast:
                    
                    temp1 = fast.next
                    length = 1
                    while(temp1 != fast):
                        length = length + 1 
                        temp1 = temp1.next
                    
                    return length
            return "No Loop Found"
    def printList(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            slow = self.head
            fast = self.head
            while(fast.next != None):
                slow = slow.next
                fast = fast.next.next

                if fast == slow:
                    temp2 = fast.next
                   
                    while(temp2 != fast):
                        print(temp2.data)
                        temp2 = temp2.next
                    print(fast.data) # this is out of loop because this node cannot be accessed in the while loop hence we just print the common node
                    return
            return "NO Loop Found"
llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fouth = Node(44)

llist.head.next = second
second.next = third
third.next = fouth
fouth.next = llist.head


print(len(llist))
print() # prints a blank line

llist.printList()