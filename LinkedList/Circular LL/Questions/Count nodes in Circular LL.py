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
                if slow == fast:
                    temp = fast.next
                    print(fast.data)
                    while(temp != fast):
                        print(temp.data) 
                        temp = temp.next
                    return
    def __len__(self):
        if self.head is None:
            return 0
        else:
            slow = self.head
            fast = self.head
            while(fast):
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    temp2 = fast.next
                    length = 1
                    while(temp2 != fast):
                        length = length + 1
                        temp2 = temp2.next
                    return length

                
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
print() # prints a blank line
print(len(llist))
