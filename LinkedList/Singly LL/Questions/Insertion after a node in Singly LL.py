class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp1 = self.head
        while(temp1):
            print(temp1.data)
            temp1 = temp1.next

    def insertAfternode(self,data,prevnode):
        new_node = Node(data)
        temp2 = self.head
        while(temp2.data != prevnode): # temp2 stops on the node whose data = prev node
            temp2 = temp2.next
            # if no node matches with prev_node and we are at the end of the linkedlist
            if temp2.data != prevnode and temp2.next == None:
                print("Prev node is not in this LinkedList")
                return
       
        new_node.next = temp2.next
        temp2.next = new_node

        
llist = LinkedList()
llist.head = Node(1)
second = Node(22)
third = Node(33)
fourth = Node(44)

llist.head.next = second
second.next = third
third.next = fourth

llist.insertAfternode(1001,22) 
llist.printList()

llist.insertAfternode(1001,44) 
llist.printList()

llist.insertAfternode(1001,99) # prev not found! 