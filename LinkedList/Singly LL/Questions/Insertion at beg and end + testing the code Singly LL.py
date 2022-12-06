class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        temp1 = self.head
        while(temp1):
            print(temp1.data)
            temp1 = temp1.next

    def insertEnd(self,data):
        new_node = Node(data)

        # if the linked list empty then this new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # traversing till the last node
        temp2 = self.head
        while(temp2.next):
            temp2 = temp2.next
        #now temp2 is pointing to the last node
        temp2.next = new_node

    def insertBeg(self,data):
        new_node = Node(data)
        # checking if the linked list is empty 
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head # new node now points to the old head node
        self.head = new_node # new header is the node we inserted at the start

        
        
llist = LinkedList()
llist.head = Node(1)
second = Node(22)
third = Node(33)
fourth = Node(44)

llist.head.next = second
second.next = third
third.next = fourth

llist.printList()

print() # prints blank line

llist.insertBeg(1001)

llist.printList()
print()

llist.insertEnd(20002)
llist.printList()