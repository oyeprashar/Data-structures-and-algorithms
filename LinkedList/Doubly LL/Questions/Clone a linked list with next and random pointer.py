#NOTE: This is an IMPORTANT interview question
# Logic to clone a LinkedList having next and random pointers
#   Algorithm:
#       1) Create a clone list with just next pointers
#       2)Now make random pointer of each node in clone list to point to node in orginal node with same data. Repeat for each node in clone
#       3) Now change the next pointers of original list. Make next of node in orginal list point to node in clone with same data. repeat all the nodes in original list.
#       4) Now random of each node shoulder pointer to node.random = node.random.random.next 
#       5) The fourth step helps us to find the corresponding random node using the orginal node in the deep copy
# IMPORTANT NOTE: first make the random pointers of next list to point to nodes in the orignal list then change the next in the orginal list else it will be a mess ##
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

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

    def copyLL(self):
       
       
        # making a new linked list with next 
        temp2 = self.head
        llist2 = LinkedList()
        new_node = Node(temp2.data)

        llist2.head = new_node
        temp3 = self.head.next
        
        while(temp3):
            new_node.next = Node(temp3.data)
            temp3 = temp3.next
            new_node = new_node.next
    
       

        # Making random pointer of clone list to point to nodes with same data in the original list
        temp7 = llist2.head
        temp8 = self.head
        while(temp8):
            temp7.random = temp8
            temp7 = temp7.next 
            temp8 = temp8.next 
         # making next of origincal list to point at nodes in the clone list (same data)
        temp5 = self.head
        temp6 = llist2.head
        while(temp5):
            next_node1 = temp5.next 
            temp5.next = temp6
            
            temp5 = next_node1
            temp6 = temp6.next

        # Now finally setting random of cloned LL to .random.random.next 
        temp9 = llist2.head
        while(temp9):
            temp9.random = temp9.random.random.next
            temp9 = temp9.next

        
        print("===CHECKING THE RANDOM POINTERS===") 
        temp9 = llist2.head
        while(temp9):
            print(temp9.data,"-->",temp9.random.data) 
            temp9 = temp9.next   

        
llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)

llist.head.next = second
second.next = third
third.next = fourth

llist.head.random = fourth
third.random = second
fourth.random = llist.head 
second.random = third

print("===ORIGINAL LIST WITH RANDOM POINTERS===")
temp99 = llist.head
while(temp99):
    print(temp99.data,"-->",temp99.random.data) 
    temp99 = temp99.next


llist.copyLL()