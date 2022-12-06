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
            temp 1 = temp1.next

    def insertEnd(self,data):
        new_node = Node(data)
        # if the the link list is empty i.e. self.head = None, the new node becomes the head
        if self.head is None:
            self.head = new_node # issko seeda head bna diya without other steps becuase linked list is empty
            return
        # if the above condition is not satisfied, we will insert node at the end
        temp2 = self.head
        while(temp2.next): # traversing the LL with pointer temp2 until the a nodes next is none (pointer stops on the node jisska next is none i.e. the last node)
            temp2 = temp2.next

        temp2.next = new_node

    
