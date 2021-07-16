# NOTE : the logic is that for the odd length of the linked list, print the data of the middle length
# for even length of the linkedlist there would be two elements in the node. Print the data of the second one.
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

    def printMidddle(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp2 = self.head
            length = 0
            while(temp2):
                length = length + 1
                temp2 = temp2.next
            if length %2 == 0:
                mid = (int(length/2))
            else:
                mid =int(length/2)
            temp3 = self.head
            for _ in range(mid): # NOTE: since temp3 is already on the first node we don't need to write range(mid+1)
                temp3 = temp3.next
            print(temp3.data)   

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
print() #prints a blank line

llist.printMidddle()