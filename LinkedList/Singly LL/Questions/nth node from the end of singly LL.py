#Logic to get nth item from the back:
# index from the back starts from 1 (actually -1), so just print the data of (len - n)th node.
# pointer is already on the head node so we dont' have to worry ki range() aakhiri include nhi karega (len-n) me
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
    
    def nthfromEnd(self,n):
        if self.head is None:
            return "LINKEDLIST EMPTY"
        else:
            temp2 = self.head
            length = 0
            while(temp2):
                length = length + 1
                temp2 = temp2.next
            if n >length:
                return "N is out of the LinkedList"
            else:
                temp3 = self.head
                for _ in range((length-n)):  
                    temp3 = temp3.next # since pointer is already on the head node so we dont' have to worry ki range() aakhiri include nhi karega (len-n) me
                return temp3.data
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

print(llist.nthfromEnd(5))