class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("EMPTY LIST")
            return
        temp1 = self.head
        while(temp1):
            print(temp1.data)
            temp1 = temp1.next

    def deleteKey(self,key):
        prev = self.head
        # if the key we want to delete is in the head node 
        if self.head.data == key:
            temp3 = self.head
            self.head = temp3.next
            del temp3

        # if the key is in any other node except the head 
        else:
            while(prev.next.data != key):
                prev = prev.next

                # agar prev pointer end tak chala gya h and data of no node matches with key then it means key is not in our linkedlist
                if prev.next == None and prev.data != key:
                    print("Key:",key, "is not in this LinkedList")
                    return 
            current = prev.next
            prev.next = current.next
            del current

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

llist.deleteKey(66)
llist.printList()
print() # this prints a blank line

llist.deleteKey(2002) # this key is not in this linkedlist
print() # prints a blank line

llist.deleteKey(11)

llist.printList()
