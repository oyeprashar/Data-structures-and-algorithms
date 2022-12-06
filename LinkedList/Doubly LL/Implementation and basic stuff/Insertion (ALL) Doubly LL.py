class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

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
            return

    def insertBeg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp2 = self.head
            while(temp2.next != None):
                temp2 = temp2.next
            
            temp2.next = new_node
            new_node.prev = temp2

    def insertafterNode(self,given_node,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp3 = self.head
            while(temp3.data != given_node):
                temp3 = temp3.next
            temp3.next.prev = new_node
            new_node.next = temp3.next
            new_node.prev = temp3
            temp3.next = new_node

    def insertBeforeNode(self,given_node,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.data != given_node):
                temp = temp.next
            temp.prev.next = new_node
            new_node.next = temp.prev
            new_node.next = temp
            temp.prev = new_node

llist = LinkedList()
llist.head = Node(11)
first = Node(22)
second = Node(33)
third = Node(44)
fourth = Node(55)
fifth = Node(66)

llist.head.next = first
first.prev = llist.head
first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

llist.printList()
print() # prints a blank line

llist.insertBeg(100)
llist.printList()
print() # prints a blank line

llist.insertEnd(200)
llist.printList()
print()

llist.insertafterNode(22,2002)
llist.printList()
print() # prints a blank line

llist.insertBeforeNode(44,100001)
llist.printList()