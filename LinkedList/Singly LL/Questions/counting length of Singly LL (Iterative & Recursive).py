class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("The LinkedList is empty!")
        else:
            temp1 = self.head
            while(temp1):
                print(temp1.data)
                temp1 = temp1.next
        
    def iterativeSize(self):
        count = 0
        if self.head is None:
            return 0
        else:
            temp2 = self.head
            while(temp2):
                count = count + 1
                temp2 = temp2.next
            return count
    def getrecuriveSize(self,node):
        # base/termination condition is when pointer is at the last node
        if node == None:
            return 0
        else:
            return 1 + self.getrecuriveSize(node.next)
    def recursiveSize(self):
        return self.getrecuriveSize(self.head)

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
print("Size using iteration",llist.iterativeSize())
print("Size using recursion",llist.recursiveSize())
print() # prints a blank line

#let llist2 be another LinkedList which has no node
llist2 = LinkedList()
print("Size using iteration",llist2.iterativeSize())
print("Size using recursion",llist2.recursiveSize())

