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

    def iterativeSearch(self,key):
        temp2 = self.head
        while(temp2):
            temp2 = temp2.next
            if temp2.data == key:
                return True
                
            elif temp2.data != key and temp2.next == None:
                return False
    def getrecursiveSearch(self,head_node,key):

        # base/terminating conditon
        if head_node is None: # if the node is None i.e. it is out of the linked list
            return False 

        #check if the current node contains the key
        if head_node.data == key:
            return True
        
        else:
            return self.getrecursiveSearch(head_node.next,key)
    
    def recursiveSearch(self,key):
        return self.getrecursiveSearch(self.head,key)
                

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

print(llist.iterativeSearch(44))
print(llist.iterativeSearch(99))
print() # prints blank line
print(llist.recursiveSearch(44))
print(llist.recursiveSearch(99))