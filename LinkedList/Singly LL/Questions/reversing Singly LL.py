# NOTE: Logic to reverse a singly linked list is:
#       since in singly linked list we dont have pointer to prev node we have to maintain two pointers
#       set curr.next =   previous_node 
#       now set previous_node = curr and increment curr
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
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
            return

    def reverseList(self):
        curr = self.head
        previous = None

        while(curr):
            if curr.next == None:
                self.head = curr

            next_noode = curr.next # saving the info about the next node before changing
            curr.next = previous # now current node points to previous node
            
            previous = curr
            curr = next_noode

            

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

print("----ORIGINAL LINKEDLIST----")
llist.printList()
print()
llist.reverseList()
print("----REVERSED LIST----")
llist.printList()