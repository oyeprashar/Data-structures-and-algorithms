### Important Note:
# By setting head to None, you've ensured that the nodes it held previously can no longer be accessed (assuming you didn't store references to them elsewhere). 
# Python will see this and automatically free the memory associated with the nodes.

class Node():
    # defining attributes of node and constructor
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    # defining the attribute
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("The LinkList is empty")
        else:
            temp1 = self.head
            while(temp1):
                print(temp1.data)
                temp1 = temp1.next

    def deleteLinkedList(self):
        if self.head is None:
            print("The LinkedList is already empty")
        else:
            self.head = None
llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(55)
sixth = Node(66)

llist.head.next = second
second.next = third
third.next= fourth
fourth.next = fifth
fifth.next = sixth

llist.printList()
print()

llist.deleteLinkedList()
llist.printList()