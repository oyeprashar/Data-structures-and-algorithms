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
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

    def insertBefore(self,given_node,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp2 = self.head
            while(temp2.next.data != given_node):
                temp2 = temp2.next
            new_node.next = temp2.next
            temp2.next = new_node

llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(55)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

llist.printList()
print() # prints a blank line

llist.insertBefore(22,20002)
llist.printList()