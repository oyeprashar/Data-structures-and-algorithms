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
            slow = self.head
            fast = self.head
            while(fast):
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    temp = fast.next
                    print(fast.data)
                    while(temp != fast):
                        print(temp.data) 
                        temp = temp.next
                    return

    def delBeg(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp2 = self.head
            while(temp2.next != self.head):
                temp2 = temp2.next
            temp2.next = self.head.next
            self.head = temp2.next 
    def delEnd(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp3 = self.head 
            while(temp3.next.next != self.head):
                temp3 = temp3.next
            temp3.next = self.head
    def delAfternode(self,node_data):
        if self.head is None:
            print("The LinkedList is already empty")
        else:
            temp4 = self.head
            while(temp4.next.data != node_data):
                temp4 = temp4.next
            temp4.next = temp4.next.next

llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(55)
sixth = Node(66)
seventh = Node(77)
eighth = Node(88)
ninth = Node(99)
tenth = Node(100)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eighth
eighth.next = ninth
ninth.next = tenth
tenth.next = llist.head

llist.printList()
print()
llist.delBeg()
llist.printList()
print()
llist.delEnd()
llist.printList()
print()
llist.delAfternode(44)
llist.printList()