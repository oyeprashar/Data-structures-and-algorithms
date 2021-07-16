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
            temp1 = self.head
            while(temp1):
                print(temp1.data) 
                temp1 = temp1.next

    def getNth(self,n):
        temp2 = self.head
        for _ in range(n):
            temp2 = temp2.next
        print(temp2.data)   

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

llist.getNth(0)
llist.getNth(1)
llist.getNth(2)
llist.getNth(3)
llist.getNth(4)
llist.getNth(5)