#NOTE: Implementation of circular linked list is same as the singly LL the only difference is that the next of last node is first forming a loop

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)

# Making a them circular
llist.head.next = second
second.next = third
third.next = llist.head

