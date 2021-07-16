# deletion of last head node
# deletion of the last node
# deletion by index number

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
    def __len__(self):
        if self.head is None:
            return 0
        else:
            length = 0
            temp1 = self.head
            while(temp1):
                length = length + 1
                temp1 = temp1.next
            return length


    def deleteBeg(self):
        if self.head is None:
            print("The LinkedList is empty!")
        else:
            temp = self.head.next
            temp.prev = None
            self.head.next = None
            self.head = temp
    def deleteEnd(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            last_node = temp.next
            temp.next = None
            last_node.prev = None

    def deleteByIndex(self,index):
        if self.head is None:
            print("The LinkedList is empty!")
        else:
            length = 0
            temp = self.head
            while(temp):
                length = length + 1
                temp = temp.next
            if index > length - 1:
                print("INDEX OUT OF LINKEDLIST")
            else:
                temp2 = self.head
                for _ in range(index):
                    temp2 = temp2.next

                
                if index == len(self)-1:
                    prev_node = temp2.prev
                    prev_node.next = None
                    temp2.prev = None
                    
                elif index == 0:
                    second_node = temp2.next
                    temp2.next = None
                    second_node.prev = None
                    self.head = second_node
                else:
                    prev_node = temp2.prev
                    next_node = temp2.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
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

print("====Removing the first node by index====")
llist.deleteByIndex(0)
llist.printList()
print()

print("====Removing the last node by index====")
llist.deleteByIndex(5)
llist.printList()
print()

print("====Removing the any  node by index====")
llist.deleteByIndex(2)
llist.printList()

