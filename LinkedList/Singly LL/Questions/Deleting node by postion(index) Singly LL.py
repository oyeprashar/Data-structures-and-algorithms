class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp1 = self.head 
            while(temp1):
                print(temp1.data)
                temp1 = temp1.next

    def deletebyPostion(self,postion):
        temp2 = self.head
        # if head node has to be deleted
        if postion == 0:
            self.head = temp2.next

            # if we want to delete any node in the linkedlist except the head
        else: 
            for _ in range(postion-1): # it will run till postion-1
                temp2 = temp2.next
            
            del_node = temp2.next
            temp2.next = del_node.next
        
llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(55)
sixth = Node(66)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

llist.printList()
print() # prints a blank line

llist.deletebyPostion(5)
llist.printList()