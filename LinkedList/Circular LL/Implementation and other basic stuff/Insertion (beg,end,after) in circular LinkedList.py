#NOTE: In circular LinkedList, inserting at the beg and end are exactly same with just one difference. For insertion at the beg of the list we need to make it the
#      head however for inserting at the end we need not to make it the head.
# 11->22->33->44->55->66->head
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            slow = self.head
            fast = self.head
            while(fast):
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    temp1 = fast.next
                    print(fast.data)
                    while(temp1 != fast):
                        print(temp1.data)
                        temp1 = temp1.next
                    return
    def insertBeg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp2 = self.head
            while(temp2.next != self.head):
                temp2 = temp2.next
            temp2.next = new_node
            new_node.next = self.head
            self.head = new_node        

    def insertEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp3 = self.head
            while(temp3.next != self.head):
                temp3 = temp3.next
            temp3.next = new_node
            new_node.next = self.head

    def insertafter(self,given_node,data):
        new_node = Node(data)
        temp4 = self.head
        while(temp4.data != given_node):
            temp4 = temp4.next
        new_node.next = temp4.next
        temp4.next = new_node
    
    def insertBefore(self,given_node,data):
        new_node = Node(data)
        temp = self.head
        while(temp.next.data != given_node):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node            

llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = llist.head

llist.printList()
print()

llist.insertBeg(10)
llist.printList()
print()

llist.insertEnd(1000)
llist.printList()
print()

llist.insertafter(33,99)
llist.printList()
print()

llist.insertBefore(22,20002)
llist.printList()