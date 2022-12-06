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
            print("The Doubly LL is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
            return
    
    def reverseList(self):
        temp = self.head
        while(temp):
            if temp.next == None:
                self.head = temp
            next_pointer = temp.next
            temp.next = temp.prev
            temp.prev = next_pointer
            temp  = temp.prev # since prev is now next (incrementing the loop variable)

            



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
print()
llist.reverseList()
llist.printList()