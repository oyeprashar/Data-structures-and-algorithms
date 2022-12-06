class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertBeg(self,data):
        new_node = Node(data)
        # making new node to point at old head
        new_node.next = self.head
        # Now making this node head of our linked list (old head is now second node)
        self.head = new_node 