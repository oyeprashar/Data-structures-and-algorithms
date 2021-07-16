# NOTE: logic to delete duplicates:
#       We will create a dictionary and since in dictionary keys cannot repeat so will get dictionary of nodes which are unique
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
    def duplicates(self):
        cur = self.head
        prev = None 
        dup_dict = {}

        while(cur):
            if cur.data in dup_dict:
                prev.next = cur.next # prev wil point to node next to cur hence cur will be removed
                
            else:
                dup_dict[cur.data] = 1
                prev = cur # NOTE: why is this satement inside else?
            cur = prev.next
# NOTE: why are we setting prev = cur when a new node is encountered that is in the else block?
    #   because we want to delete the copies, let the node with duplicate data be 'D' and next node of 'D' be 'E' so, when we ecounter a non-duplicate node
    #   our prev pointer is set to that( and when we find unique node i.e. it is not in our dictionary, our else block will run), now when we encounter 'D', 
    #   the next of prev will be set to next of 'D' that is 'E' and node 'D' is removed from our linked list.
llist = LinkedList()

llist.head = Node(12)
second = Node(11)
third = Node(12)
fourth = Node(12)
fifth = Node(21)
sixth = Node(21)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

llist.duplicates()
llist.printList()


